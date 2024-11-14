from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker, declarative_base

# Création du moteur et de la base
Base = declarative_base()

class Categorie(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False, unique=True)
    produits = relationship('Produit', back_populates='categorie')

class Produit(Base):
    __tablename__ = 'produits'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False)
    prix = Column(Float, nullable=False)
    categorie_id = Column(Integer, ForeignKey('categories.id'))
    categorie = relationship('Categorie', back_populates='produits')

class Type_Paiement(Base):
    __tablename__ = 'type_paiements'
    id = Column(Integer, primary_key=True)
    nom = Column(String, nullable=False, unique=True) 

class BaseDeDonnees:
    def __init__(self, nom_bd='sqlite:///bdd.db'):
        self.engine = create_engine(nom_bd)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    # Ajout d'une catégorie
    def ajouter_categorie(self, nom):
        categorie = Categorie(nom=nom)
        self.session.add(categorie)
        self.session.commit()
        return categorie

    # Ajout d'un produit
    def ajouter_produit(self, nom, prix, categorie_id):
        produit = Produit(nom=nom, prix=prix, categorie_id=categorie_id)
        self.session.add(produit)
        self.session.commit()
        return produit

    # Ajout d'un paiement
    def ajouter_type_paiement(self, nom):
        type_paiement = Type_Paiement(nom=nom)
        self.session.add(type_paiement)
        self.session.commit()
        return type_paiement

    # Lecture d'une catégorie
    def lire_categorie(self, categorie_id):
        return self.session.query(Categorie).filter_by(id=categorie_id).first()

    # Lecture d'un produit
    def lire_produit(self, produit_id):
        return self.session.query(Produit).filter_by(id=produit_id).first()

    # Lecture d'un paiement
    def lire_type_paiement(self, paiement_id):
        return self.session.query(Type_Paiement).filter_by(id=paiement_id).first()

    # Mise à jour d'une catégorie
    def mettre_a_jour_categorie(self, categorie_id, nom):
        categorie = self.lire_categorie(categorie_id)
        if categorie:
            categorie.nom = nom
            self.session.commit()
        return categorie

    # Mise à jour d'un produit
    def mettre_a_jour_produit(self, produit_id, nom, prix, categorie_id):
        produit = self.lire_produit(produit_id)
        if produit:
            produit.nom = nom
            produit.prix = prix
            produit.categorie_id = categorie_id
            self.session.commit()
        return produit

    # Mise à jour d'un paiement
    def mettre_a_jour_type_paiement(self, paiement_id, methode):
        type_paiement = self.lire_type_paiement(paiement_id)
        if type_paiement:
            type_paiement.methode = methode
            self.session.commit()
        return type_paiement

    # Suppression d'une catégorie
    def supprimer_categorie(self, categorie_id):
        categorie = self.lire_categorie(categorie_id)
        if categorie:
            self.session.delete(categorie)
            self.session.commit()

    # Suppression d'un produit
    def supprimer_produit(self, produit_id):
        produit = self.lire_produit(produit_id)
        if produit:
            self.session.delete(produit)
            self.session.commit()

    # Suppression d'un paiement
    def supprimer_type_paiement(self, type_paiement_id):
        type_paiement = self.lire_paiement(type_paiement_id)
        if type_paiement:
            self.session.delete(type_paiement)
            self.session.commit()

    # Liste de toutes les catégories
    def lister_categories(self):
        return self.session.query(Categorie).all()

    # Liste de tous les produits
    def lister_produits(self):
        return self.session.query(Produit).all()

    def lister_produits_par_categorie(self, categorie_nom):
        # Rechercher l'instance de Categorie correspondant au nom
        categorie = self.session.query(Categorie).filter_by(nom=categorie_nom).first()
        if categorie:
            # Utiliser l'ID de la catégorie pour filtrer les produits
            return self.session.query(Produit).filter_by(categorie_id=categorie.id).all()
        return []

    # Liste de tous les paiements
    def lister_type_paiements(self):
        return self.session.query(Type_Paiement).all()

# Exemple d'utilisation
if __name__ == "__main__":
    import os
    os.chdir(os.path.dirname(__file__))
    if not os.path.exists("bdd.db"):
        bd = BaseDeDonnees()
        
        # Ajout d'une catégorie
        nouvelle_categorie = bd.ajouter_categorie("Boissons")
        nouveau_produit = bd.ajouter_produit("Coca-Cola", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Fanta", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Orangina", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Sprite", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Coca cherry", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Red-bull", 3.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Jus de pomme", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Jus de fraise", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Jus de raisin", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Jus multifruit", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Biere", 3, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Eau", 0.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Eau Gazeuse", 0.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Thé", 2.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Rhum", 4.5, nouvelle_categorie.id)

        
        
        nouvelle_categorie = bd.ajouter_categorie("Snack")
        nouveau_produit = bd.ajouter_produit("Burger", 5.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Hot-dog", 4.5, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Chips", 2, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Gateau", 1.5, nouvelle_categorie.id)
        
        
        nouvelle_categorie = bd.ajouter_categorie("Restaurant")
        nouveau_produit = bd.ajouter_produit("Tartiflette", 10, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Raclette", 15, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Fish & chips", 7, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Pate bolo", 6, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Bavette", 10, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Entrecote", 15, nouvelle_categorie.id)
        nouveau_produit = bd.ajouter_produit("Fondue", 9, nouvelle_categorie.id)
        
        bd.ajouter_type_paiement("Carte de crédit")
        bd.ajouter_type_paiement("Chéque")
        bd.ajouter_type_paiement("Liquide")
        bd.ajouter_type_paiement("Ticket restau")
