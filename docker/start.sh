#!/bin/sh

# Environment variables
export PG_VERSION=14
export PG_BINDIR=/usr/lib/postgresql/$PG_VERSION/bin
export PGDATA=/var/lib/postgresql/$PG_VERSION/main

# Initialize PostgreSQL if needed
if [ ! -d "$PGDATA" ]; then
    sudo -u postgres initdb -D $PGDATA
fi

# Start PostgreSQL
echo "Starting PostgreSQL..."
sudo -u postgres $PG_BINDIR/pg_ctl start --pgdata=$PGDATA

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
psql -U postgres -c "DO \$\$ BEGIN CREATE ROLE pscompose_user WITH LOGIN PASSWORD 'password'; EXCEPTION WHEN duplicate_object THEN null; END \$\$;"

# Create the database if it doesn't already exist
echo "Creating the database..."
createdb -U postgres -O pscompose_user pscompose

# Create the database if it doesn't already exist
# echo "Creating the database..."
# sudo -u postgres createdb pscompose

# Set Python Path to include /app
export PYTHONPATH="/app"

# Create tables in PostgreSQL
echo "Running table creation script..."
python3 /app/pscompose/create_tables.py

# Q : Should we extract database name from settings.py?
# DB_NAME=$(python3 -c "from pscompose.settings import POSTGRES_DB_NAME; print(POSTGRES_DB_NAME)")
# sudo -u postgres createdb "$DB_NAME"

# TODO: Run FastAPI
# exec = pass process control to child process
# exec fastapi run /app/pscompose/api/api.py --port 80
# for now, don't exec it
fastapi run /app/pscompose/api/api.py --port 80

# exec a forever command instead
exec tail -f /dev/null