""" Routes for the endpoint 'event'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.event.models import EventModel
from data.event.schemas import EventSchema
from shared import db

NAME = 'event'

event_blueprint = Blueprint(f"{NAME}_event_blueprint", __name__)


@event_blueprint.get(f"/get_event/<int:id>")
def get_event(id: str):
    """GET route code goes here"""
    entity: EventModel = db.session.query(EventModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@event_blueprint.post(f"/add_event/")
def post_event():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: EventModel = EventSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid EventModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return EventSchema().dump(entity), 200


@event_blueprint.delete(f"/delete_vent/<int:id>")
def delete_event(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@event_blueprint.put(f"/update_event/<int:id>")
def put_event(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@event_blueprint.patch(f"/modify_event/<int:id>")
def patch_event(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
