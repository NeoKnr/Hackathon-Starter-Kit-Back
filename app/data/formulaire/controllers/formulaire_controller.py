""" Routes for the endpoint 'formulaire'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.formulaire.models import FormulaireModel
from data.formulaire.schemas import FormulaireSchema
from shared import db

NAME = 'formulaire'

formulaire_blueprint = Blueprint(f"{NAME}_formulaire_blueprint", __name__)


@formulaire_blueprint.get(f"/get_formulaire/<int:id>")
def get_formulaire(id: str):
    """GET route code goes here"""
    entity: FormulaireModel = db.session.query(FormulaireModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@formulaire_blueprint.post(f"/add_formulaire/")
def post_formulaire():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: FormulaireModel = FormulaireSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid FormulaireModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return FormulaireSchema().dump(entity), 200


@formulaire_blueprint.delete(f"/delete_formulaire/<int:id>")
def delete_formulaire(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@formulaire_blueprint.put(f"/update_formulaire/<int:id>")
def put_formulaire(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@formulaire_blueprint.patch(f"/modify_formulaire/<int:id>")
def patch_formulaire(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
