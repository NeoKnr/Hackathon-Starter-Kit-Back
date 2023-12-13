""" Routes for the endpoint 'hello_world'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.dossier.models import DossierModel
from data.dossier.schemas import DossierSchema
from shared import db

NAME = 'dossier'

dossier_blueprint = Blueprint(f"{NAME}_dossier_blueprint", __name__)


@dossier_blueprint.get(f"/get_dossier/<int:id>")
def get_hello_world(id: str):
    """GET route code goes here"""
    entity: DossierModel = db.session.query(DossierModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@dossier_blueprint.post(f"/add_dossier/")
def post_dossier():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: DossierModel = DossierSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid DossierModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return DossierSchema().dump(entity), 200


@dossier_blueprint.delete(f"/delete_dossier/<int:id>")
def delete_dossier(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@dossier_blueprint.put(f"/update_dossier/<int:id>")
def put_dossier(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@dossier_blueprint.patch(f"/modify_dossier/<int:id>")
def patch_dossier(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
