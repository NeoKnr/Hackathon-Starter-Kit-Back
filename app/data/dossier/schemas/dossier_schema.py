"""Schema for serializing/deserializing a HelloWorldModel"""

from data.dossier.models.dossier_model import DossierModel
from shared.utils.schema.base_schema import BaseSchema


class DossierSchema(BaseSchema):
    class Meta:
        model = DossierModel
        load_instance = True