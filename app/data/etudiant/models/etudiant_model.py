from sqlalchemy import Column, String, Integer

from shared import db


class EtudiantModel(db.Model):
    __tablename__ = "etudiant"
    id_etudiant = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nom = Column(String(100), nullable = False)
    nom = Column(String(100), nullable = False)
    email = Column(String(200), nullable = False, unique = True)
    mot_de_passe = Column(String(32), nullable = False)
    classe = Column(String(50), nullable = False)
