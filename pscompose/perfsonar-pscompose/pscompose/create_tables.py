from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pscompose.models import SQLAlchemyStorage
from pscompose.settings import DATABASE_URL

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()
# Create all tables in the database
SQLAlchemyStorage.metadata.create_all(bind=engine)
session.commit()

print("Tables created successfully!")
