"""Schema for serializing/deserializing a HelloWorldModel"""

from data.photo.models.photo_model import Photo
from shared.utils.schema.base_schema import BaseSchema


class PhotoSchema(BaseSchema):
    class Meta:
        model = Photo
        load_instance = True