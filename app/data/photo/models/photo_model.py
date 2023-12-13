from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from shared import db

class Photo(db.Model):
    __tablename__ = 'photo'
    idPhoto = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nomPhoto = Column(String(100), nullable = False)
    date = Column(DateTime, nullable = False)
    typePhoto = Column(String(50), nullable = False)
    idDossier = Column(Integer, ForeignKey('dossier.idDossier'))
    dossier = relationship("Dossier", back_populates="photo")
