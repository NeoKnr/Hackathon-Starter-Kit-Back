"""Schema for serializing/deserializing a HelloWorldModel"""

from data.photo.models.photo_model import PhotoModel
from shared.utils.schema.base_schema import BaseSchema


class PhotoSchema(BaseSchema):
    class Meta:
        model = PhotoModel
        load_instance = True