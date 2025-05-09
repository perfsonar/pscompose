#!/bin/sh

# Environment variables
export PG_VERSION=14

# Since path is different for macbooks with apple chip vs intel chip
export PG_PREFIX=$(brew --prefix postgresql@$PG_VERSION)
export PG_BINDIR="$PG_PREFIX/bin"
export PGDATA="$(brew --prefix)/var/postgresql@$PG_VERSION"

# Initialize PostgreSQL if needed
if [ ! -d "$PGDATA/base" ]; then
    echo "Initializing PostgreSQL data directory at $PGDATA..."
    $PG_BINDIR/initdb -D "$PGDATA"
fi

# Start PostgreSQL if not running
if ! pg_isready; then
    echo "Starting PostgreSQL..."
    brew services start postgresql@$PG_VERSION
    sleep 2
fi

# Wait for PostgreSQL to be ready
until pg_isready -h localhost -p 5432; do
    echo "Waiting for PostgreSQL to be ready..."
    sleep 2
done

# Create postgres superuser if it doesn't exist
echo "Creating postgres superuser..."
createuser -s postgres

# Create the user if it doesn't exist
echo "Creating pscompose_user..."
# TODO : CHECK this line?
psql -U postgres -c "DO \$\$ BEGIN CREATE ROLE pscompose_user WITH LOGIN PASSWORD 'password'; EXCEPTION WHEN duplicate_object THEN null; END \$\$;"

# Create the database if it doesn't already exist
echo "Creating the database..."
createdb -U postgres -O pscompose_user pscompose

# Grant necessary permissions
echo "Granting permissions..."
psql -U postgres -d pscompose -c "GRANT ALL PRIVILEGES ON DATABASE pscompose TO pscompose_user;"
psql -U postgres -d pscompose -c "GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO pscompose_user;"
psql -U postgres -d pscompose -c "GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO pscompose_user;"

# Set Python Path to include the current directory
export PYTHONPATH="$(pwd)"

# Create tables in PostgreSQL
echo "Running table creation script..."
python3 pscompose/create_tables.py

# Seed dummy data
echo "Seeding dummy data..."
python3 pscompose/seed_data.py
