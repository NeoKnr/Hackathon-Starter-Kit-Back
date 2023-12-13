""" Routes for the endpoint 'promotion'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.promotion.models import PromotionModel
from data.promotion.schemas import PromotionSchema
from shared import db

NAME = 'promotion'

promotion_blueprint = Blueprint(f"{NAME}_promotion_blueprint", __name__)


@promotion_blueprint.get(f"/get_promotion/<int:id>")
def get_promotion(id: str):
    """GET route code goes here"""
    entity: PromotionModel = db.session.query(PromotionModel).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@promotion_blueprint.post(f"/add_promotion/")
def post_promotion():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: PromotionModel = PromotionSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid PromotionModel: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return PromotionSchema().dump(entity), 200


@promotion_blueprint.delete(f"/delete_promotion/<int:id>")
def delete_promotion(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@promotion_blueprint.put(f"/update_promotion/<int:id>")
def put_promotion(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@promotion_blueprint.patch(f"/modify_promotion/<int:id>")
def patch_promotion(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
