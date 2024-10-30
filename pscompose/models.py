from typing import Dict, List, Any, Optional
from pydantic import BaseModel as PydanticValidationModel
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.dialects import postgresql
from enum import Enum

from sqlalchemy import create_engine, Column, LargeBinary, Integer, Text

from pscompose.settings import POSTGRES_USER_NAME, POSTGRES_DB_NAME, TOKEN_SCOPES

# Pydantic Validation Model subclasses will model input and output types from the API.
# SQLAlchemy Storage subclasses will model data as stored in the DB.

engine = create_engine(
    "postgresql://%s@/%s" % (POSTGRES_USER_NAME, POSTGRES_DB_NAME)
)

SQLAlchemyStorage = declarative_base()

class ScopeEnum(str, Enum):
    read = TOKEN_SCOPES["read"]
    write = TOKEN_SCOPES["write"]
    publish = TOKEN_SCOPES["publish"]
    admin = TOKEN_SCOPES["admin"]


class UserUpdate(PydanticValidationModel):
    '''User Update models the data needed for the situation where a User receives an update.'''
    username: str
    name: str
    scopes: List[ScopeEnum]


class UserCreate(UserUpdate):
    '''User Create models the data needed for the situation where a User is created from scratch. Includes "password."'''
    password: str


class User(UserUpdate):
    '''User models user data as returned by the API.'''
    pass


class PasswordReset(PydanticValidationModel):
    '''Password Reset just validates that a user password has been sent.'''
    password: str


class UserTable(SQLAlchemyStorage):
    '''The UserTable model defines what's actually stored in the Postgres 'user' table.'''
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    # username used to store both email and username
    username = Column(Text)
    name = Column(Text)
    password = Column(LargeBinary(60))
    scopes = Column(postgresql.JSON)
