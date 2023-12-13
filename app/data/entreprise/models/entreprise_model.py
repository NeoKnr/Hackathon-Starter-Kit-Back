from sqlalchemy import Column, String, Integer

from shared import db

class Entreprise(db.Model):
    __tablename__ = "entreprise"
    idEntreprise = Column(Integer, primary_key = True, unique = True, nullable = False)
    nomEntreprise = Column(String(200), unique = True, nullable = False)
    logo = Column(String(200), unique = True, nullable = False)
    site = Column(String(200), unique = True, nullable = False)
    adresse = Column(String(200), unique = True, nullable = False)
    telephone = Column(String(20), unique = True, nullable = False)
    categorieEntreprise = Column(String(100), nullable = False)