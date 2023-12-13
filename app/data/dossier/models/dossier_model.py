from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from shared import db

class Dossier(db.Model):
    __tablename__ = 'dossier'
    idDossier = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nomDossier = Column(String(100), nullable = False, unique = True)
    Date = Column(DateTime, nullable = False)
    idEvent = Column(Integer, ForeignKey('event.idEvent'))
    event = relationship("Event", back_populates="dossiers")