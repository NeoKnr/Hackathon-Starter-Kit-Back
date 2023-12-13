"""Schema for serializing/deserializing a HelloWorldModel"""

from data.etudiant.models.etudiant_model import Etudiant
from shared.utils.schema.base_schema import BaseSchema


class EtudiantSchema(BaseSchema):
    class Meta:
        model = Etudiant
        load_instance = True