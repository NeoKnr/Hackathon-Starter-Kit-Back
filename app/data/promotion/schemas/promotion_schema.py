"""Schema for serializing/deserializing a HelloWorldModel"""

from data.promotion.models.promotion_model import Promotion
from shared.utils.schema.base_schema import BaseSchema


class PromotionSchema(BaseSchema):
    class Meta:
        model = Promotion
        load_instance = True