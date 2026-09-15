#!/bin/sh
#
# Sets up the PostgreSQL database for pscompose on a fresh install.
# - Generates a random password for pscompose_user
# - Writes the password into /etc/perfsonar/pscompose/settings.yml
# - Creates the PostgreSQL role, database, and grants permissions
# - Runs the table creation script using the installed venv
#
# Must be run as root or the PostgreSQL superuser.
# Safe to run only on fresh installs; will not overwrite an existing database
# or an already-configured password in settings.yml.
#

WHOAMI=$(basename "$0")
SETTINGS_FILE="/etc/perfsonar/pscompose/settings.yml"
VENV_PYTHON="/usr/lib/perfsonar/pscompose/venv/bin/python3"
PSCOMPOSE_DIR="/usr/lib/perfsonar/pscompose"
DB_NAME="pscompose"
DB_USER="pscompose_user"

die()
{
    echo "${WHOAMI}: $*" 1>&2
    exit 1
}

TMPBASE=$(mktemp -d)
chmod 755 "${TMPBASE}"
cleanup()
{
    rm -rf "${TMPBASE}"
}
trap cleanup EXIT

# ---------------------------------------------------------------------------
# Check: only run on fresh installs (skip if database already exists)
# ---------------------------------------------------------------------------
# Detect the PostgreSQL superuser
PG_USER=$(ps -e -o 'user,command' \
    | awk '$2 == "postgres:" { print $1 }' \
    | sort -u \
    | head -1)
if [ -z "${PG_USER}" ]
then
    die "Unable to determine PostgreSQL user. Is PostgreSQL running?"
fi

[ "$(id -nu)" = "${PG_USER}" ] || [ "$(id -u)" = "0" ] \
    || die "This program must be run as root or ${PG_USER}"

# Helper: run a SQL command as the PostgreSQL superuser.
# Writes SQL to a temp file to safely handle multi-line statements and quoting.
# Optional second argument is the database to connect to (defaults to postgres).
run_sql()
{
    local sql="$1"
    local db="${2:-postgres}"
    printf '%s\n' "${sql}" > "${TMPBASE}/cmd.sql"
    chmod 644 "${TMPBASE}/cmd.sql"
    if [ "$(id -u)" = "0" ]
    then
        su - "${PG_USER}" -c "PGOPTIONS='--client-min-messages=warning' \
            psql -q -v ON_ERROR_STOP=1 -d '${db}' -f '${TMPBASE}/cmd.sql'" \
            2>"${TMPBASE}/error"
    else
        PGOPTIONS='--client-min-messages=warning' \
            psql -q -v ON_ERROR_STOP=1 -d "${db}" -f "${TMPBASE}/cmd.sql" \
            2>"${TMPBASE}/error"
    fi
}

# Check if the database already exists — if so, skip setup to avoid clobbering
DB_EXISTS=$(run_sql "SELECT 1 FROM pg_database WHERE datname='${DB_NAME}';" \
    | grep -c "^ *1" || true)
# -----------------------------------------------------------------------
# Determine the password to use.
# Always read it from settings.yml if already set; generate one if not.
# This runs unconditionally so we can sync the password to PostgreSQL
# even when the database already exists (e.g. after a failed install).
# -----------------------------------------------------------------------
if [ ! -f "${SETTINGS_FILE}" ]
then
    die "Settings file not found: ${SETTINGS_FILE}"
fi

EXISTING_PW=$(grep -A5 '^database:' "${SETTINGS_FILE}" 2>/dev/null \
    | awk -F': *' '/password:/ { print $2; exit }' \
    | tr -d "' \"")

if [ -n "${EXISTING_PW}" ] && [ "${EXISTING_PW}" != "password" ]
then
    echo "${WHOAMI}: Using password already set in ${SETTINGS_FILE}."
    PG_PASSWORD="${EXISTING_PW}"
else
    # Generate a 32-character random alphanumeric password
    PG_PASSWORD=$(tr -dc 'A-Za-z0-9' < /dev/urandom | head -c 32)
    sed -i "s|^\(\s*password:\s*\).*|\1${PG_PASSWORD}|" "${SETTINGS_FILE}" \
        || die "Failed to write password to ${SETTINGS_FILE}"
    chown root:perfsonar "${SETTINGS_FILE}"
    chmod 0640 "${SETTINGS_FILE}"
    echo "${WHOAMI}: Generated password written to ${SETTINGS_FILE}"
fi

if [ "${DB_EXISTS}" -gt 0 ]
then
    echo "${WHOAMI}: Database '${DB_NAME}' already exists, skipping database/role creation."
else
    # -----------------------------------------------------------------------
    # Create PostgreSQL role, database, and grant permissions
    # -----------------------------------------------------------------------
    echo "${WHOAMI}: Creating database '${DB_NAME}'..."
    run_sql "CREATE DATABASE ${DB_NAME};" \
        || die "Failed to create database: $(cat "${TMPBASE}/error")"

    echo "${WHOAMI}: Granting permissions..."
    run_sql "GRANT ALL PRIVILEGES ON DATABASE ${DB_NAME} TO ${DB_USER};" \
        || die "Failed to grant database privileges: $(cat "${TMPBASE}/error")"

    # Connect to the new database to grant schema-level permissions
    run_sql "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO ${DB_USER};
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO ${DB_USER};
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO ${DB_USER};
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO ${DB_USER};" \
        "${DB_NAME}" \
        || die "Failed to grant schema privileges: $(cat "${TMPBASE}/error")"

fi  # end fresh-install block

# -----------------------------------------------------------------------
# Always create/update the role with the current password, using
# scram-sha-256 hashing.  This is idempotent and fixes any mismatch
# between the password in settings.yml and what PostgreSQL has stored
# (e.g. if the role was previously created with md5 hashing).
# -----------------------------------------------------------------------
echo "${WHOAMI}: Syncing PostgreSQL role '${DB_USER}' password..."
run_sql "SET password_encryption = 'scram-sha-256';
DO \$\$
BEGIN
  IF EXISTS (SELECT 1 FROM pg_roles WHERE rolname = '${DB_USER}') THEN
    ALTER ROLE ${DB_USER} WITH LOGIN PASSWORD '${PG_PASSWORD}';
  ELSE
    CREATE ROLE ${DB_USER} WITH LOGIN PASSWORD '${PG_PASSWORD}';
  END IF;
END
\$\$;" \
    || die "Failed to create/update role: $(cat "${TMPBASE}/error")"

# ---------------------------------------------------------------------------
# Configure pg_hba.conf to allow pscompose_user to authenticate with
# scram-sha-256.  We use the drop-in tool (from the drop-in package) so
# that the entries are idempotent and are inserted BEFORE any catch-all
# rules that would otherwise take precedence.
# ---------------------------------------------------------------------------
echo "${WHOAMI}: Configuring pg_hba.conf..."

# Ask PostgreSQL for the path to its HBA file.
# Use -At (tuples-only, unaligned) so we get just the bare path, nothing else.
if [ "$(id -u)" = "0" ]
then
    PG_HBA=$(su - "${PG_USER}" -c \
        "psql -At -c 'SHOW hba_file;'" 2>/dev/null | tr -d '[:space:]')
else
    PG_HBA=$(psql -At -c 'SHOW hba_file;' 2>/dev/null | tr -d '[:space:]')
fi
if [ -z "${PG_HBA}" ]
then
    die "Could not determine pg_hba.conf path"
fi

drop-in -t -n pscompose - "${PG_HBA}" <<EOF
# pscompose: allow pscompose_user to authenticate locally
local   pscompose      pscompose_user                              scram-sha-256
host    pscompose      pscompose_user      127.0.0.1/32            scram-sha-256
host    pscompose      pscompose_user      ::1/128                 scram-sha-256
EOF
[ $? -eq 0 ] || die "drop-in failed to update ${PG_HBA}"

# Reload PostgreSQL so the new HBA rules take effect.
echo "${WHOAMI}: Reloading PostgreSQL configuration..."
run_sql "SELECT pg_reload_conf();" \
    || die "Failed to reload PostgreSQL configuration"

# ---------------------------------------------------------------------------
# Create tables using the installed venv
# ---------------------------------------------------------------------------
echo "${WHOAMI}: Running table creation script..."
PYTHONPATH="${PSCOMPOSE_DIR}" \
PSCOMPOSE_SETTINGS="${SETTINGS_FILE}" \
    "${VENV_PYTHON}" -m pscompose.create_tables \
    || die "Table creation script failed"

echo "${WHOAMI}: Setup complete."
