
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

from gestionData import JsonStoreDatabase

bdd = JsonStoreDatabase()

# Gestion d'import des différentes fenêtres
class Fenetre_Principale(Screen):
    def on_pre_enter(self, **kwargs):
        super(Fenetre_Principale, self).__init__(**kwargs)
        self.afficherCategories()

    def afficherCategories(self):
        categories = bdd.get_all_categories()
        for cat in categories:
            self.ids.liste_categories.add_widget(Button(text=cat))

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
            bdd.add_category(nom_categorie)
        else:
            print("Champ vide")
        
class CaisseApp(App):
    def build(self):
        # Création d'un ScreenManager pour gérer les transitions
        self.sm = ScreenManager()
        self.sm.add_widget(Fenetre_Principale(name='Fenetre_Principale'))
        self.sm.add_widget(Fenetre_Configuration(name='Fenetre_Configuration'))
        self.sm.add_widget(Fenetre_Categories(name='Fenetre_Categories'))
        return self.sm
    
if __name__ == '__main__':
    
    CaisseApp().run()