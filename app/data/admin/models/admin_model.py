from sqlalchemy import Column, String, Integer

from shared import db

class Admin(db.Model):
    __tablename__ = "admin"
    idAdmin = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nom = Column(String(100), nullable = False)
    prenom = Column(String(100), nullable = False)
    email = Column(String(200), nullable = False, unique = True)
    motDePasse = Column(String(32), nullable = False)
    role = Column(String(50), nullable = False)
