"""Schema for serializing/deserializing a HelloWorldModel"""

from data.promotion.models.promotion_model import PromotionModel
from shared.utils.schema.base_schema import BaseSchema


class PromotionSchema(BaseSchema):
    class Meta:
        model = PromotionModel
        load_instance = True