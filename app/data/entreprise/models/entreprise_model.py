from sqlalchemy import Column, String, Integer

from shared import db

class EntrepriseModel(db.Model):
    __tablename__ = "entreprise"
    id_entreprise = Column(Integer, primary_key = True, unique = True, nullable = False)
    nom_entreprise = Column(String(200), unique = True, nullable = False)
    logo = Column(String(200), unique = True, nullable = False)
    site = Column(String(200), unique = True, nullable = False)
    adresse = Column(String(100), unique = True, nullable = False)
    code_postal = Column(Integer, nullable = False)
    ville = Column(String(50), nullable = False)
    telephone = Column(String(20), unique = True, nullable = False)
    categorie_entreprise = Column(String(100), nullable = False)