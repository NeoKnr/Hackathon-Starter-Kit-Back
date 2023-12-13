""" Routes for the endpoint 'entreprise'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.entreprise.models import EntrepriseModel
from data.entreprise.schemas import EntrepriseSchema
from shared import db

NAME = 'entreprise'

entreprise_blueprint = Blueprint(f"{NAME}_entreprise_blueprint", __name__)


@entreprise_blueprint.get(f"/get_entreprise/<int:id>")
def get_entreprise(id: str):
    """GET route code goes here"""
    entity: EntrepriseModel = db.session.query(EntrepriseModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@entreprise_blueprint.post(f"/add_entreprise/")
def post_entreprise():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: EntrepriseModel = EntrepriseSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid EntrepriseModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return EntrepriseSchema().dump(entity), 200


@entreprise_blueprint.delete(f"/delete_entreprise/<int:id>")
def delete_entreprise(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@entreprise_blueprint.put(f"/update_entreprise/<int:id>")
def put_entreprise(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@entreprise_blueprint.patch(f"/modify_entreprise/<int:id>")
def patch_entreprise(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
