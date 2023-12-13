""" Routes for the endpoint 'etudiant'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.etudiant.models import EtudiantModel
from data.etudiant.schemas import EtudiantSchema
from shared import db

NAME = 'etudiant'

etudiant_blueprint = Blueprint(f"{NAME}_etudiant_blueprint", __name__)


@etudiant_blueprint.get(f"/get_etudiant/<int:id>")
def get_etudiant(id: str):
    """GET route code goes here"""
    entity: EtudiantModel = db.session.query(EtudiantModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@etudiant_blueprint.post(f"/add_etudiant/")
def post_etudiant():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: EtudiantModel = EtudiantSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid EtudiantModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return EtudiantSchema().dump(entity), 200


@etudiant_blueprint.delete(f"/delete_etudiant/<int:id>")
def delete_etudiant(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@etudiant_blueprint.put(f"/update_etudiant/<int:id>")
def put_etudiant(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@etudiant_blueprint.patch(f"/modify_etudiant/<int:id>")
def patch_etudiant(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
