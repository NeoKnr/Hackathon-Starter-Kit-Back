from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from shared import db

class PromotionModel(db.Model):
    __tablename__ = "promotion"
    id_promotion = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    intitule = Column(String(200), nullable = False)
    description = Column(String(1000), nullable = False)
    debut_promotion = Column(DateTime, nullable = False)
    fin_promotion = Column(DateTime, nullable = False)
    id_entreprise = Column(Integer, ForeignKey('entreprise.id_entreprise'))
    entreprise = relationship("Entreprise", back_populates="promotions")
