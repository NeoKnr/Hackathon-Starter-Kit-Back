from sqlalchemy import Column, String, Integer, DateTime, ForeignKey

from shared import db

class PhotoModel(db.Model):
    __tablename__ = 'photo'
    id_photo = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nom_photo = Column(String(100), nullable = False)
    date = Column(DateTime, nullable = False)
    type_photo = Column(String(50), nullable = False)
