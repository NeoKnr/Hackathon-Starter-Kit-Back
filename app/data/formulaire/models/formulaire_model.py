from sqlalchemy import Column, String, Integer

from shared import db

class FormulaireModel(db.Model):
    __tablename__ = "formulaire"
    id_formulaire = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nom = Column(String(100), nullable = False)
    prenom = Column(String(100), nullable = False)
    email = Column(String(200), nullable = False)
    objet = Column(String(200), nullable = False)
    message = Column(String(2000), nullable = False)