from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from shared import db

class Dossier(db.Model):
    __tablename__ = 'dossier'
    id_dossier = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nom_dossier = Column(String(100), nullable = False, unique = True)
    date = Column(DateTime, nullable = False)
    id_event = Column(Integer, ForeignKey('event.idEvent'))
    event = relationship("Event", back_populates="dossiers")
    photos = relationship("Photo", back_populates="dossier")