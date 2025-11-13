from pscompose import create_tables
from pscompose.settings import DATABASE_URL
from sqlalchemy import inspect


def test_tables_created():
    assert create_tables


def test_using_sqlite():
    assert "sqlite" in DATABASE_URL


def test_metadata_table_created():
    inspector = inspect(create_tables.engine)
    schemas = inspector.get_schema_names()
    table_names = inspector.get_table_names(schema=schemas[0])
    assert "data" in table_names
    assert "user" in table_names
