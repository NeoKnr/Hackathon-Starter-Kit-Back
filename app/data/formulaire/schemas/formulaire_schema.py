"""Schema for serializing/deserializing a HelloWorldModel"""

from data.formulaire.models.formulaire_model import FormulaireModel
from shared.utils.schema.base_schema import BaseSchema


class FormulaireSchema(BaseSchema):
    class Meta:
        model = FormulaireModel
        load_instance = True