from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from shared import db

class Promotion(db.Model):
    __tablename__ = "promotion"
    idPromotion = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    intitulé = Column(String(200), nullable = False)
    description = Column(String(1000), nullable = False)
    debutPromotion = Column(DateTime,nullable = False)
    finPromotion = Column(DateTime,nullable = False)
    idEntreprise = Column(Integer, ForeignKey('entreprise.idEntreprise'),
    entreprise = relationship("Entreprise", back_populates="promotions"))
