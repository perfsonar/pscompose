import yaml
import os
import sys
import random
import string

DEFAULT_CONFIG_FILE = "/etc/pscompose/settings.yml"

CONFIG_FILENAME = os.environ.get("PSCOMPOSE_SETTINGS", DEFAULT_CONFIG_FILE)
LOGLEVEL = os.environ.get("LOGLEVEL", "WARNING").upper()

conf = None
try:
    with open(CONFIG_FILENAME) as f:
        conf = yaml.safe_load(f)
except Exception as e:
    print(f"Unable to read config file {CONFIG_FILENAME} -- {e}")
    sys.exit(1)

if conf is None:
    conf = {}

POSTGRES = conf.get("postgres", {})  # default to empty dict so we can set further defaults
AUTH = conf.get("auth", {})

POSTGRES_DB_NAME = POSTGRES.get("db_name", "pscompose")
POSTGRES_USER_NAME = POSTGRES.get("user_name", "postgres")

TOKEN_SCOPES = {
    "read": AUTH.get("read_scope", "pscompose:read"),
    "write": AUTH.get("write_scope", "pscompose:write"),
    "publish": AUTH.get("publish_scope", "pscompose:publish"),
    "admin": AUTH.get("admin_scope", "pscompose:admin"),
}

class DataTypes:
    TEMPLATE = "template"
    TASK = "task"
    SCHEDULE = "schedule"
    ARCHIVE = "archive"
    CONTEXT = "context"
    GROUP = "group"
    HOST = "host"
    TEST = "test"

PARENT_CHILD_RELATIONSHIP = {
    # TODO : Is it hosts or addresses?
    # "template": ["archive", "host", "group", "schedule", "test", "task", "context"],
    "template": ["archive", "address", "group", "schedule", "test", "task", "context"],
    "archive": [],
    "context": [],
    "group": ["address"],
    # "address": [],
    # "host": ["address", "context"],
    "schedule": [],
    "task": ["group", "test", "schedule", "archive"],
    "test": []
}
