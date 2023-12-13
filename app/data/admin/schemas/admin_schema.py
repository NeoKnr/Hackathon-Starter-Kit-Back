"""Schema for serializing/deserializing a HelloWorldModel"""

from data.admin.models.admin_model import AdminModel
from shared.utils.schema.base_schema import BaseSchema


class AdminSchema(BaseSchema):
    class Meta:
        model = AdminModel
        load_instance = True