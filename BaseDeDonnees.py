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

    def init_db_test(self):
        # Ajout d'une catégorie
        nouvelle_categorie = self.ajouter_categorie("Boissons")
        nouveau_produit = self.ajouter_produit("Coca-Cola", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Fanta", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Orangina", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Sprite", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Coca cherry", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Red-bull", 3.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Jus de pomme", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Jus de fraise", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Jus de raisin", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Jus multifruit", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Biere", 3, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Eau", 0.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Eau Gazeuse", 0.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Thé", 2.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Rhum", 4.5, nouvelle_categorie.id)

        
        
        nouvelle_categorie = self.ajouter_categorie("Snack")
        nouveau_produit = self.ajouter_produit("Burger", 5.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Hot-dog", 4.5, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Chips", 2, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Gateau", 1.5, nouvelle_categorie.id)
        
        
        nouvelle_categorie = self.ajouter_categorie("Restaurant")
        nouveau_produit = self.ajouter_produit("Tartiflette", 10, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Raclette", 15, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Fish & chips", 7, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Pate bolo", 6, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Bavette", 10, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Entrecote", 15, nouvelle_categorie.id)
        nouveau_produit = self.ajouter_produit("Fondue", 9, nouvelle_categorie.id)
        
        self.ajouter_moyen_paiement("Carte de crédit")
        self.ajouter_moyen_paiement("Chéque")
        self.ajouter_moyen_paiement("Liquide")
        self.ajouter_moyen_paiement("Ticket restau")

    # Ajout d'une catégorie
    def ajouter_categorie(self, nom):
        if not nom == "":
            try:
                categorie = Categorie(nom=nom)
                self.session.add(categorie)
                self.session.commit()
                return categorie
            except Exception as e:
                self.session.rollback()
                return f"ERREUR : {e}"
        else:
            return "Champ vide"


    # Ajout d'un produit
    def ajouter_produit(self, nom, prix, categorie_id):
        produit = Produit(nom=nom, prix=prix, categorie_id=categorie_id)
        self.session.add(produit)
        self.session.commit()
        return produit

    # Ajout d'un moyen paiement
    def ajouter_moyen_paiement(self, nom):
        if not nom == "":
            try:
                moyen_paiement = Type_Paiement(nom=nom)
                self.session.add(moyen_paiement)
                self.session.commit()
                return moyen_paiement
            except Exception as e:
                self.session.rollback()
                return f"ERREUR : {e}"
        else:
            return "Champ vide"


    # Lecture d'une catégorie
    def lire_categorie(self, categorie_id):
        return self.session.query(Categorie).filter_by(id=categorie_id).first()

    # Lecture d'un produit
    def lire_produit(self, produit_id):
        return self.session.query(Produit).filter_by(id=produit_id).first()

    # Lecture d'un paiement
    def lire_moyen_paiement(self, paiement_id):
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
    def mettre_a_jour_moyen_paiement(self, paiement_id, methode):
        type_paiement = self.lire_moyen_paiement(paiement_id)
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
    def supprimer_moyen_paiement(self, type_paiement_id):
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
    def lister_moyen_paiements(self):
        return self.session.query(Type_Paiement).all()

