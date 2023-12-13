"""Schema for serializing/deserializing a HelloWorldModel"""

from data.event.models.event_model import Event
from shared.utils.schema.base_schema import BaseSchema


class EventSchema(BaseSchema):
    class Meta:
        model = Event
        load_instance = True