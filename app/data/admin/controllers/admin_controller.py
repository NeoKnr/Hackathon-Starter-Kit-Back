""" Routes for the endpoint 'hello_world'"""

from flask import Blueprint, request
from marshmallow import ValidationError

from data.admin.models import Admin
from data.admin.schemas import AdminSchema
from shared import db

NAME = 'admin'

admin_blueprint = Blueprint(f"{NAME}_admin_blueprint", __name__)


@admin_blueprint.get(f"/get_admin/<int:id>")
def get_admin(id: str):
    """GET route code goes here"""
    entity: Admin = db.session.query(Admin).get(id)
    if entity is None:
        return "Goodby, World.", 404
    return entity.message, 200


@admin_blueprint.post(f"/add_admin/")
def post_admin():
    """POST route code goes here"""
    payload = request.get_json()
    try:
        entity: Admin = AdminSchema().load(payload)
    except ValidationError as error:
        return f"The payload does't correspond to a valid Admin: {error}", 400
    db.session.add(entity)
    db.session.commit()
    return AdminSchema().dump(entity), 200


@admin_blueprint.delete(f"/delete_admin/<int:id>")
def delete_admin(id: str):
    """DELETE route code goes here"""
    return "Unimplemented", 501


@admin_blueprint.put(f"/update_admin/<int:id>")
def put_admin(id: str):
    """PUT route code goes here"""
    return "Unimplemented", 501


@admin_blueprint.patch(f"/modify_admin/<int:id>")
def patch_admin(id: str):
    """PATCH route code goes here"""
    return "Unimplemented", 501
