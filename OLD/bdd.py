from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


import os 

# Database connection
DATABASE = 'sqlite:///db.sqlite3'
DEBUG = True

# ORM base
db = declarative_base()

# Connect to database
engine = create_engine(DATABASE, echo=DEBUG)
session_factory = sessionmaker(bind=engine)
session = session_factory()


class GestionBDD:
   
    def listeTout(self, table):
        liste = session.query(table).all()
        return liste
    
    def ajouter(self, table, form):
        instance = table(**form)  # Créez une instance du modèle de table spécifié avec les données du formulaire
        session.add(instance)  # Ajoutez l'instance à la session SQLAlchemy
        session.commit()       # Enregistrez les changements dans la base de données
        return instance

    def update(self, table, id, form):
        ligne = session.query(table).filter_by(id=id)
        formAvt = self.get_by_id(table, id).to_dict()
        ligne.update(form)
        session.commit()
   
    def supprimer(self, table, id):
        ligne = session.query(table).get(id) 
        session.delete(ligne)
        session.commit()

    def get_by_id(self, table, id):
        return session.query(table).get(id)


class Categories(db, GestionBDD):
    __tablename__ = 'table_categorie'
    nom_table = "Table Demande"
    id = Column(Integer, primary_key=True, autoincrement=True)
    nom = Column(String, nullable=False)

class Produits(db, GestionBDD):
    __tablename__ = 'table_produits'
    nom_table = "Table Produits"

    id = Column(Integer, primary_key=True)
    categorie = Column(String, nullable=False)
    nom = Column(String, nullable=False)
    prix = Column(Float, nullable=False)
    


# Initialize database if it doesn't exist
if not os.path.exists('db.sqlite3'):
    db.metadata.create_all(engine)

# Example usage:
liste_categories = Categories().listeTout(Categories)  # Passer la classe 'Categories' en paramètre
