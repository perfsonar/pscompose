from sqlalchemy import create_engine
from pscompose.models import SQLAlchemyStorage
from pscompose.models import UserTable, DataTable  # import your models
from pscompose.settings import POSTGRES_USER_NAME, POSTGRES_DB_NAME

# Use the same DATABASE_URL defined in your models.py or environment variable
# DB_HOST = "postgres"  # Service name from docker-compose.yml
DB_HOST = "localhost"
DB_PORT = 5432
DB_USER = POSTGRES_USER_NAME
DB_NAME = POSTGRES_DB_NAME
DB_PASSWORD = "password"  # Fetch securely in production
DATABASE_URL = f"postgresql+psycopg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
# DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create all tables in the database
SQLAlchemyStorage.metadata.create_all(bind=engine)

print("Tables created successfully!")