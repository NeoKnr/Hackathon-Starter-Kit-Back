import sys
import traceback

from marshmallow import ValidationError

from shared import db
from data.common.schema import BaseSchema


class BaseCRUDHelper:
    """Utility class for basic CRUD operations on an SQLAlchemy data model."""
    def __init__(self, model: type, schema: BaseSchema):
        self.schema = schema
        self.model = model
        self.name = self.model.__tablename__

    def save_to_db(self, entity):
        db.session.add(entity)
        db.session.commit()
        return entity

    def get_from_db(self, id):
        return db.session.get(self.model, id, with_for_update=True)

    def handle_get(self, id):
        entity = self.get_from_db(id)
        if not entity:
            return {'error': f'No {self.name} found with id={id}'}, 404
        return_value = self.schema.dump(entity)
        return return_value, 200

    def handle_delete(self, id):
        entity = self.get_from_db(id)
        if entity:
            db.session.delete(entity)
            db.session.commit()
            return {"message": 'success'}, 200
        return {"message": f"{self.name} not found"}, 404

    def handle_put(self, id, data):
        try:
            entity = self.get_from_db(id)
            if not entity:
                return {"message": f"{self.name} not found"}, 404
            self.schema.load(data, instance=entity, partial=True)
            db.session.add(entity)
            db.session.commit()
            return self.schema.dump(entity), 200
        except ValidationError as e:
            return {'error': f'Data validation error: {e}'}, 400
        except Exception as e:
            traceback.print_exc()
            sys.stdout.flush()
            return {'error': f'Server Error: {e}'}, 500

    def handle_post(self, data):
        try:
            entity = self.schema.load(data)
            db.session.add(entity)
            db.session.commit()
            return {'id': entity.id, 'status': 'success'}, 201
        except ValidationError as e:
            return {'error': f'Data validation error: {e}'}, 400
        except Exception as e:
            traceback.print_exc()
            sys.stdout.flush()
            return {'error': f'Server Error: {e}'}, 500