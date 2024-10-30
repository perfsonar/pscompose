#!/bin/sh

export PG_VERSION=14
export PG_BINDIR=/usr/lib/postgresql/$PG_VERSION/bin
export PGDATA=/var/lib/postgresql/$PG_VERSION/main

sudo -u postgres $PG_BINDIR/pg_ctl start --pgdata=$PGDATA
sudo -u postgres createdb pscompose
# exec = pass process control to child process
# exec fastapi run /app/pscompose/api/api.py --port 80
# for now, don't exec it
fastapi run /app/pscompose/api/api.py --port 80
# exec a forever command instead
exec cat /dev/null