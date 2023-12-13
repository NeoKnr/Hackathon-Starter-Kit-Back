""" Routes for the endpoint 'photo'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.photo.models import PhotoModel
from data.photo.schemas import PhotoSchema
from shared import db

NAME = 'photo'

photo_blueprint = Blueprint(f"{NAME}_photo_blueprint", __name__)


@photo_blueprint.get(f"/get_photo/<int:id>")
def get_photo(id: str):
    """GET route code goes here"""
    entity: PhotoModel = db.session.query(PhotoModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@photo_blueprint.post(f"/add_photo/")
def post_photo():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: PhotoModel = PhotoSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid PhotoModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return PhotoSchema().dump(entity), 200


@photo_blueprint.delete(f"/delete_photo/<int:id>")
def delete_photo(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@photo_blueprint.put(f"/update_photo/<int:id>")
def put_photo(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@photo_blueprint.patch(f"/modify_photo/<int:id>")
def patch_photo(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
