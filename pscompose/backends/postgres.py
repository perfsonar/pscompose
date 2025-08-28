from pscompose.models import DataTable, engine
from pscompose.schemas import DataTableUpdate
from sqlalchemy.orm import sessionmaker, declarative_base
from pscompose.settings import DataTypes
from fastapi import Depends, HTTPException
from sqlalchemy import func

class PostgresBackend:
    """
    This class is intended to provide connectivity to a postgreSQL database.
    Specifically, the table that stores all the data outside of users
    """

    def __init__(self):
        DataTable.__table__.create(bind=engine, checkfirst=True)
        self.session = sessionmaker(bind=engine)()

    def create_datatype(self, ref_set, datatype, json, name, created_by, last_edited_by):
        try:
            new_type = DataTable(
                ref_set = ref_set,
                type = datatype,
                json = json,
                name = name,
                created_by = created_by,
                last_edited_by = last_edited_by,
                # created_at = created_at,
                # last_edited_at = last_edited_at,
                # url = url
            )
            self.session.add(new_type)
            self.session.commit()
            return new_type
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=422, detail=f"Could not create the {type}")

    def update_datatype(self, existing_result, updated_data):
        try:
            updated_dict = updated_data.dict(exclude_unset=True, by_alias=True)
            for field, value in updated_dict.items():
                setattr(existing_result, field, value)

            self.session.commit()

            return {
                "id": existing_result.id,
                "type": existing_result.type,
                "name": existing_result.name,
                "json": existing_result.json,
                "ref_set": existing_result.ref_set,
                "last_edited_by": existing_result.last_edited_by,
                "last_edited_at": existing_result.last_edited_at
            }
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to update record: {str(e)}")
    
    def delete_datatype(self, res):
        try:
            self.session.delete(res)
            self.session.commit()
            return {"message": f"Record with {res.id} deleted successfully"}
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=f"Failed to delete record: {str(e)}")
    
    def find_records(self, target_id):
        """
        Find all records in the database where the ref_set contains the given target_id.
        """
        try:
            # Query to find records where target_id is in ref_set
            query = self.session.query(DataTable).filter(
                target_id == func.any(DataTable.ref_set)
            ).order_by(DataTable.created_at.desc())
            results = query.all()
            if not results:
                raise HTTPException(status_code=422, detail=f"No records found with {target_id} in ref_set")
            return results
        except Exception as e:
            self.session.rollback()
            raise HTTPException(status_code=500, detail=f"An error occurred while querying the database: {str(e)}")

    def get_results(self, datatype):
        query = self.session.query(DataTable).filter_by(type=datatype).order_by(DataTable.created_at.desc())
        rows = query.all()
        return [row for row in rows]
    
    def get_datatype(self, datatype, item_id):
        query = self.session.query(DataTable).filter_by(type=datatype)
        if item_id:
            query = query.filter_by(id=item_id)

        result = query.first()
        if not result:
            raise HTTPException(status_code=404, detail=f"No records found for id : {id}")
        else:
            return result


backend = PostgresBackend()
