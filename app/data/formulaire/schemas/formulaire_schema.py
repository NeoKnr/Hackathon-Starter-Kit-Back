"""Schema for serializing/deserializing a HelloWorldModel"""

from data.admin.models.admin_model import Formulaire
from shared.utils.schema.base_schema import BaseSchema


class FormulaireSchema(BaseSchema):
    class Meta:
        model = Formulaire
        load_instance = True