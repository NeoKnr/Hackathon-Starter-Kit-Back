"""Schema for serializing/deserializing a HelloWorldModel"""

from data.dossier.models.dossier_model import Dossier
from shared.utils.schema.base_schema import BaseSchema


class DossierSchema(BaseSchema):
    class Meta:
        model = Dossier
        load_instance = True