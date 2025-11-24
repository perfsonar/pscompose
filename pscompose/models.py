import uuid

from enum import Enum
from typing import List
from sqlalchemy.orm import declarative_base
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.mutable import MutableDict, MutableList
from pydantic import BaseModel as PydanticValidationModel
from pscompose.settings import DATABASE_URL, TOKEN_SCOPES
from sqlalchemy import (
    create_engine,
    Column,
    LargeBinary,
    Integer,
    Text,
    Boolean,
    String,
    DateTime,
    func,
    ARRAY,
    JSON,
)

# Pydantic Validation Model subclasses will model input and output types from the API.
# SQLAlchemy Storage subclasses will model data as stored in the DB.

engine = create_engine(DATABASE_URL)

# engine = create_engine(
#     "postgresql+psycopg://%s@/%s" % (POSTGRES_USER_NAME, POSTGRES_DB_NAME)
# )

SQLAlchemyStorage = declarative_base()


class ScopeEnum(str, Enum):
    read = TOKEN_SCOPES["read"]
    write = TOKEN_SCOPES["write"]
    publish = TOKEN_SCOPES["publish"]
    admin = TOKEN_SCOPES["admin"]


class UserUpdate(PydanticValidationModel):
    """User Update models the data needed for the situation where a User receives an update."""

    username: str
    name: str
    scopes: List[ScopeEnum]


class UserCreate(UserUpdate):
    '''User Create models the data needed for the situation where a User is created from scratch.
    Includes "password."'''

    password: str


class User(UserUpdate):
    """User models user data as returned by the API."""

    pass


class PasswordReset(PydanticValidationModel):
    """Password Reset just validates that a user password has been sent."""

    password: str


class UserTable(SQLAlchemyStorage):
    """The UserTable model defines what's actually stored in the Postgres 'user' table."""

    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    # username used to store both email and username
    username = Column(Text)
    name = Column(Text)
    password = Column(LargeBinary(60))
    scopes = Column(postgresql.JSON)


def generate_uuid():
    """Generate a 12 character UUID by truncating a standard UUID"""
    return str(uuid.uuid4()).replace("-", "")[:12]


if "sqlite" in DATABASE_URL:
    ref_column = Column(MutableList.as_mutable(JSON))
else:
    ref_column = Column(MutableList.as_mutable(ARRAY(String)))


class DataTable(SQLAlchemyStorage):
    """The DataTable model defines what's stored in the Postgres 'data' table."""

    __tablename__ = "data"
    id = Column(String(12), primary_key=True, default=generate_uuid)
    ref_set = ref_column
    type = Column(Text)
    json = Column(MutableDict.as_mutable(JSON))
    name = Column(Text, nullable=False)
    url = Column(Text)
    created_by = Column(Text)
    created_at = Column(
        DateTime(timezone=True),  # Stores timezone-aware timestamps
        # func.now() retrieves the current timestamp from the database server
        server_default=func.now(),
        nullable=False,  # enforces that every record has a timestamp
    )
    last_edited_by = Column(Text)
    last_edited_at = Column(
        DateTime(timezone=True),  # Stores timezone-aware timestamps
        # func.now() retrieves the current timestamp from the database server
        server_default=func.now(),
        # Automatically updates the column to the current timestamp whenever the record is updated
        onupdate=func.now(),
        nullable=False,  # enforces that every record has a timestamp
    )
    favorited = Column(Boolean, default=False)
