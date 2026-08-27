import os
import sys
import yaml

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

ENVIRONMENT = conf.get("environment", "production")
DATABASE = conf.get("database", {})  # default to empty dict so we can set further defaults
AUTH = conf.get("auth", {})

DATABASE_NAME = DATABASE.get("db_name", "pscompose")
DATABASE_USER = DATABASE.get("user_name", "pscompose_user")
DATABASE_HOST = DATABASE.get("host", "localhost")
DATABASE_PORT = DATABASE.get("port", 5432)
DATABASE_PASSWORD = DATABASE.get("password", "password")

DATABASE_URL = f"postgresql+psycopg://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"  # noqa: E501

if ENVIRONMENT == "test":
    # allow config to override postgres connection string in testing environments
    DATABASE_URL = DATABASE.get("connection_string", DATABASE_URL)

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
    TEST = "test"
    ADDRESS = "address"


PARENT_CHILD_RELATIONSHIP = {
    "archive": [],
    "context": [],
    "schedule": [],
    "test": [],
    "address": ["context"],
    "group": ["address"],
    "task": ["group", "test", "schedule", "archive"],
    "template": ["task"],
    # "template": ["archive", "address", "group", "schedule", "test", "task", "context"],
}
