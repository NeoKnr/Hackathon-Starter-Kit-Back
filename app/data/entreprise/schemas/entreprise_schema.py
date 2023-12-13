"""Schema for serializing/deserializing a HelloWorldModel"""

from data.enteprise.models.entreprise_model import Entreprise
from shared.utils.schema.base_schema import BaseSchema


class EntrepriseSchema(BaseSchema):
    class Meta:
        model = Entreprise
        load_instance = True