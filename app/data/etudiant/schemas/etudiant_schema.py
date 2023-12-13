"""Schema for serializing/deserializing a HelloWorldModel"""

from data.etudiant.models.etudiant_model import EtudiantModel
from shared.utils.schema.base_schema import BaseSchema


class EtudiantSchema(BaseSchema):
    class Meta:
        model = EtudiantModel
        load_instance = True