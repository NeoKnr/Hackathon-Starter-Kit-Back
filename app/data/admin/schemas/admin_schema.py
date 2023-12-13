"""Schema for serializing/deserializing a HelloWorldModel"""

from data.admin.models.admin_model import Admin
from shared.utils.schema.base_schema import BaseSchema


class AdminSchema(BaseSchema):
    class Meta:
        model = Admin
        load_instance = True