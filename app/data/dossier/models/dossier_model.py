from sqlalchemy import Column, String, Integer, DateTime, ForeignKey


from shared import db

class DossierModel(db.Model):
    __tablename__ = 'dossier'
    id_dossier = Column(Integer, primary_key = True, unique = True, nullable = False, autoincrement=True)
    nom_dossier = Column(String(100), nullable = False, unique = True)
    date = Column(DateTime, nullable = False)