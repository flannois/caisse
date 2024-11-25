
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.dropdown import DropDown
from BaseDeDonnees import BaseDeDonnees


import os


def flashPopUp(msg):
    # create content and add to the popup
    
    content = Button(text=str(msg))
    popup = Popup(title="Alerte", content=content, auto_dismiss=False)

    # bind the on_press event of the button to the dismiss function
    content.bind(on_press=popup.dismiss)

    # open the popup
    popup.open()

# Gestion d'import des différentes fenêtres
class Fenetre_Principale(Screen):
    def on_pre_enter(self, **kwargs):
        super(Fenetre_Principale, self).__init__(**kwargs)
        
        self.afficherCategories()
        self.afficherTypePaiements()
        

    def afficherCategories(self):
        self.ids.liste_categories.clear_widgets()
        categories = bdd.lister_categories()
        for cat in categories:
            btn = Button(text=cat.nom)
            btn.on_press = lambda nom=cat.nom: self.afficherProduits(nom)
            btn.background_color = "red"
            self.ids.liste_categories.add_widget(btn)

    def afficherProduits(self, categorie):
        self.ids.liste_produits.clear_widgets()
        produits = bdd.lister_produits_par_categorie(categorie)
        for prod in produits:
            btn = Button(text=prod.nom)
            btn.background_color = "green"
            self.ids.liste_produits.add_widget(btn)

           
    def afficherTypePaiements(self):
        self.ids.liste_moyen_paiements.clear_widgets()
        type_paiements = bdd.lister_moyen_paiements()
        for paie in type_paiements:
            btn = Button(text=paie.nom)
            
            btn.background_color = "blue"
            self.ids.liste_moyen_paiements.add_widget(btn)

class Fenetre_Options(Screen):
    pass

class Fenetre_Produit(Screen):
    def on_pre_enter(self):
        # Options à ajouter dans le DropDown
        categories = bdd.lister_categories()

        for cat in categories:
            btn = Button(text=cat.nom, size_hint_y=None, height=44)
            # Ajouter une action au clic
            btn.bind(on_release=lambda btn: self.select_categorie(btn))
            self.ids.liste_categorie_produit.add_widget(btn)

    def select_categorie(self, cat):
        cat.background_color='green'
        self.categorie_id_a_ajouter = 1                             # A changer par l'id de la categorie
        print(f"Vous avez sélectionné : {cat}")

    def ajouter_produit(self):
        nom = self.ids.label_nom_produit.text

        prix = self.ids.label_prix_produit.text

        self.categorie_id_a_ajouter = 1                             # A changer par l'id de la categorie
        categorie_id = self.categorie_id_a_ajouter

        bdd.ajouter_produit(nom, prix, categorie_id)
        flashPopUp(f"Produit {nom} ajouté")

class Fenetre_Categories(Screen):
    def on_pre_enter(self, **kwargs):
        super(Fenetre_Categories, self).__init__(**kwargs)

    def ajouter_categorie(self):
        # Récupérer le nom de la catégorie
        nom_categorie = self.ids.label_ajout_categorie.text
        if not nom_categorie == "":
            self.ids.label_ajout_categorie.text = ""
            bdd.ajouter_categorie(nom_categorie)
            flashPopUp(f"Catégorie {nom_categorie} ajouté")

        else:
            flashPopUp("Champ vide")
 
class Fenetre_Paiements(Screen):
    def on_pre_enter(self, **kwargs):
        super(Fenetre_Paiements, self).__init__(**kwargs)

    def ajouter_paiement(self):
        # Récupérer le nom de la catégorie
        nom_paiement = self.ids.label_ajout_paiement.text
        if not nom_paiement == "":
            self.ids.label_ajout_paiement.text = ""
            bdd.ajouter_moyen_paiement(nom_paiement)
            flashPopUp(f"Paiment {nom_paiement} ajouté")
        else:
            flashPopUp("Champ vide")

class CaisseApp(App):
    def build(self):

        # Création d'un ScreenManager pour gérer les transitions
        self.sm = ScreenManager()
        self.sm.add_widget(Fenetre_Principale(name='Fenetre_Principale'))
        self.sm.add_widget(Fenetre_Options(name='Fenetre_Options'))
        self.sm.add_widget(Fenetre_Categories(name='Fenetre_Categories'))
        self.sm.add_widget(Fenetre_Paiements(name='Fenetre_Paiements'))
        self.sm.add_widget(Fenetre_Produit(name='Fenetre_Produit'))
        
        
        return self.sm
    
if __name__ == '__main__':
    
    os.chdir(os.path.dirname(__file__))
    os.remove("bdd.db")

    bdd = BaseDeDonnees()
    
    bdd.init_db_test()

    CaisseApp().run()