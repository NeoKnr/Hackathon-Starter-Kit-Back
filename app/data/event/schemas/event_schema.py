"""Schema for serializing/deserializing a HelloWorldModel"""

from data.event.models.event_model import EventModel
from shared.utils.schema.base_schema import BaseSchema


class EventSchema(BaseSchema):
    class Meta:
        model = EventModel
        load_instance = True