from pscompose.models import DataTable, engine
from sqlalchemy.orm import sessionmaker, declarative_base
from pscompose.settings import DataTypes
from fastapi import Depends, HTTPException

class PostgresBackend:
    """
    This class is intended to provide connectivity to a postgreSQL database.
    Specifically, the table that stores all the data outside of users
    """

    def __init__(self):
        DataTable.__table__.create(bind=engine, checkfirst=True)
        self.session = sessionmaker(bind=engine)()

    def get_results(self, type):
        query = self.session.query(DataTable).filter_by(type=type)
        rows = query.all()
        return rows
    
    def create_datatype(self, ref_set, type, json, name, created_by, last_edited_by):
        try:
            new_type = DataTable(
                ref_set = ref_set,
                type = type,
                json = json,
                name = name,
                created_by = created_by,
                # created_at = "",
                last_edited_by = last_edited_by,
                # last_edited_at = ""
            )
            self.session.add(new_type)
            self.session.commit()
            # What to return?
            return new_type
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=422, detail=f"Could not create the {type}")

    def get_datatype(self, type, id):
        query = self.session.query(DataTable).filter_by(type=type)
        if id:
            query = query.filter_by(id=id)

        result = query.first()
        if not result:
            raise HTTPException(status_code=422, detail="Invalid request. No results found")
        else:
            return result

    def get_datatype_json(self, type, id):
        result = self.get_datatype(type, id)
        return result.json

    def update_datatype(self, res, ref_set=None, json=None, name=None, last_edited_by=None):
        if ref_set:
            res.ref_set = ref_set
        if json:
            res.json = json
        if name:
            res.name = name
        if last_edited_by:
            res.last_edited_by = last_edited_by
        self.session.commit()

        return # What to return
    
    def delete_datatype(self, res):
        self.session.delete(res)
        self.session.commit()

        return # What to return


backend = PostgresBackend()
