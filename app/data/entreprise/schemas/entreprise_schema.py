"""Schema for serializing/deserializing a EntrepriseModel"""

from data.entreprise.models.entreprise_model import EntrepriseModel
from shared.utils.schema.base_schema import BaseSchema


class EntrepriseSchema(BaseSchema):
    class Meta:
        model = EntrepriseModel
        load_instance = True