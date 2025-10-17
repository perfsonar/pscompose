from fastapi import HTTPException
from sqlalchemy.orm import sessionmaker
from pscompose.models import DataTable, engine
from pscompose.schemas import DataTableBase
from pydantic import ValidationError


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
                ref_set=ref_set,
                type=datatype,
                json=json,
                name=name,
                created_by=created_by,
                last_edited_by=last_edited_by,
                # created_at = created_at,
                # last_edited_at = last_edited_at,
                # url = url
            )
            self.session.add(new_type)
            self.session.commit()
            return new_type
        except Exception:
            self.session.rollback()
            raise HTTPException(status_code=422, detail=f"Could not create the {datatype}")

    def update_datatype(self, existing_result, updated_data):
        try:
            updated_dict = updated_data.dict(exclude_unset=True, by_alias=True)
            for field, value in updated_dict.items():
                setattr(existing_result, field, value)

            try:
                # Validate the full ORM object
                DataTableBase.from_orm(existing_result)
            except ValidationError as ve:
                # Roll back any DB changes if validation fails
                self.session.rollback()
                # Raise a 422 error with detailed Pydantic errors
                raise HTTPException(status_code=422, detail=ve.errors())

            self.session.commit()
            self.session.refresh(existing_result)

            return {
                "id": existing_result.id,
                "type": existing_result.type,
                "name": existing_result.name,
                "json": existing_result.json,
                "ref_set": existing_result.ref_set,
                "last_edited_by": existing_result.last_edited_by,
                "last_edited_at": existing_result.last_edited_at,
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
            query = (
                self.session.query(DataTable)
                .filter(DataTable.ref_set.any(target_id))
                .order_by(DataTable.created_at.desc())
            )
            results = query.all()
            return results
        except Exception as e:
            self.session.rollback()
            raise HTTPException(
                status_code=500, detail=f"An error occurred while querying the database: {str(e)}"
            )

    def update_json(self, obj, target_id):
        """
        Recursively remove all references to target_id in:
            - dicts with 'name': target_id
            - lists of dicts
            - lists of strings/IDs
        """
        if isinstance(obj, dict):
            new_dict = {}
            for k, v in obj.items():
                new_dict[k] = self.update_json(v, target_id)
            return new_dict
        elif isinstance(obj, list):
            new_list = []
            for item in obj:
                if isinstance(item, dict) and item.get("name") == target_id:
                    continue
                elif isinstance(item, str) and item == target_id:
                    continue
                else:
                    new_list.append(self.update_json(item, target_id))
            return new_list
        else:
            return obj

    def remove_references(self, target_id: str):
        """
        Remove target_id from all ref_set arrays and the JSON where it appears
        """
        try:
            records = self.find_records(target_id)
            for record in records:
                # Remove from JSON recursively
                if isinstance(record.json, dict):
                    cleaned_json = self.update_json(record.json, target_id)
                    record.json = cleaned_json

                    try:
                        # Validate the full ORM object
                        DataTableBase.from_orm(record)
                    except ValidationError as ve:
                        # Roll back any DB changes if validation fails
                        self.session.rollback()
                        # Raise a 422 error with detailed Pydantic errors
                        raise HTTPException(
                            status_code=422,
                            detail=f"Cleanup would invalidate record {record.id}: {ve.errors()}",
                        )

                if target_id in record.ref_set:
                    record.ref_set.remove(target_id)

                print(f"Updated record {record.id}, updated ref_set:", record.ref_set)
                print(f"Updated record {record.id}, updated json:", record.json)

            self.session.commit()
            return {"message": f"Removed {target_id} from {len(records)} record(s)"}
        except Exception as e:
            self.session.rollback()
            raise HTTPException(
                status_code=500, detail=f"Failed to remove references for {target_id}: {str(e)}"
            )

    def get_results(self, datatype):
        query = (
            self.session.query(DataTable)
            .filter_by(type=datatype)
            .order_by(DataTable.created_at.desc())
        )
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
