from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pscompose.models import SQLAlchemyStorage
from pscompose.settings import DATABASE_URL


def create_tables():
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()
    SQLAlchemyStorage.metadata.create_all(bind=engine)
    session.commit()
    print("Tables created successfully!")


if __name__ == "__main__":
    create_tables()
