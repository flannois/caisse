
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

from BaseDeDonnees import BaseDeDonnees

bdd = BaseDeDonnees()

# Gestion d'import des différentes fenêtres
class Fenetre_Principale(Screen):
    def on_pre_enter(self, **kwargs):
        super(Fenetre_Principale, self).__init__(**kwargs)
        self.afficherCategories()
        self.afficherTypePaiements()
        

    def afficherCategories(self):
        categories = bdd.lister_categories()
        for cat in categories:
            btn = Button(text=cat.nom)
            btn.on_press = lambda nom=cat.nom: self.afficherProduits(nom)

            self.ids.liste_categories.add_widget(btn)

    def afficherProduits(self, categorie):
        self.ids.liste_produits.clear_widgets()
        produits = bdd.lister_produits_par_categorie(categorie)
        for prod in produits:
            self.ids.liste_produits.add_widget(Button(text=prod.nom))

    def afficherTypePaiements(self):
        type_paiements = bdd.lister_type_paiements()
        for paie in type_paiements:
            self.ids.liste_type_paiements.add_widget(Button(text=paie.nom))

class Fenetre_Configuration(Screen):
    pass

class Fenetre_Categories(Screen):
    def on_pre_enter(self, **kwargs):
        super(Fenetre_Categories, self).__init__(**kwargs)

    def ajouter_categorie(self):
        # Récupérer le nom de la catégorie
        nom_categorie = self.ids.label_ajout_categorie.text
        if not nom_categorie == "":
            self.ids.label_ajout_categorie.text = ""
            print(nom_categorie)
            bdd.ajouter_categorie(nom_categorie)
        else:
            print("Champ vide")
 
class Fenetre_Paiements(Screen):
    def on_pre_enter(self, **kwargs):
        super(Fenetre_Paiements, self).__init__(**kwargs)

    def ajouter_paiement(self):
        # Récupérer le nom de la catégorie
        nom_paiement = self.ids.label_ajout_paiement.text
        if not nom_paiement == "":
            self.ids.label_ajout_paiement.text = ""
            
            bdd.ajouter_type_paiement(nom_paiement)
        else:
            print("Champ vide")


class CaisseApp(App):
    def build(self):

        # Création d'un ScreenManager pour gérer les transitions
        self.sm = ScreenManager()
        self.sm.add_widget(Fenetre_Principale(name='Fenetre_Principale'))
        self.sm.add_widget(Fenetre_Configuration(name='Fenetre_Configuration'))
        self.sm.add_widget(Fenetre_Categories(name='Fenetre_Categories'))
        self.sm.add_widget(Fenetre_Paiements(name='Fenetre_Paiements'))
        
        return self.sm
    
if __name__ == '__main__':
    
    CaisseApp().run()