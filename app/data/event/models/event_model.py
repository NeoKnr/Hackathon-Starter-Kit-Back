from sqlalchemy import Column, String, Integer, DateTime

from shared import db

class Event(db.Model):
    __tablename__ = "event"
    idEvent = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nomEvent = Column(String(100), nullable = False)
    date = Column(DateTime, nullable = False)
    horaire = Column(DateTime, nullable = False)
    lieu = Column(String(200), nullable = False)
    photo = Column(String(200), nullable = False)
    description = Column(String(500), nullable = False)
