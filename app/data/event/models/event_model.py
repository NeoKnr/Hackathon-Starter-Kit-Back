from sqlalchemy import Column, String, Integer, DateTime

from shared import db

class EventModel(db.Model):
    __tablename__ = "event"
    id_event = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nom_event = Column(String(100), nullable = False)
    date = Column(DateTime, nullable = False)
    horaire = Column(DateTime, nullable = False)
    adresse = Column(String(100), unique = True, nullable = False)
    code_postal = Column(Integer, nullable = False)
    ville = Column(String(50), nullable = False)
    photo = Column(String(200), nullable = False)
    description = Column(String(500), nullable = False)

