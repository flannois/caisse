from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button

# Gestion d'import des différentes fenêtres
class Fenetre_Principale(Screen):
    def __init__(self, **kwargs):
        super(Fenetre_Principale, self).__init__(**kwargs)

    def updateCategories(self):
        self.ids.produits.clear_widgets()

        self.ids.produits.add_widget(Button(text="LOLOLO"))


class Fenetre_Configuration(Screen):
    pass

class Fenetre_Nouveau_Produit(Screen):
    def ajouter_un_produit(self):
        print("J'ai ajouté un produit")

        # Rediriger vers la fenêtre de configuration
        app = App.get_running_app()
        app.sm.current = 'Fenetre_Configuration'  # Change l'écran courant

    def supprimer_un_produit(self):
        print("J'ai supprimé un produit")

        # Rediriger vers la fenêtre de configuration
        app = App.get_running_app()
        app.sm.current = 'Fenetre_Configuration'  # Change l'écran courant



class Fenetre_Categories(Screen):
    def __init__(self, **kwargs):
        super(Fenetre_Categories, self).__init__(**kwargs)

    def ajouter_une_categorie(self):
        nom_categorie = self.ids.label_ajout_categorie.text
        print(f"Récupération event {nom_categorie}")
        
class Fenetre_Suppression(Screen):
    pass


# Gestionnaire d'écran
class CaisseApp(App):
    
    def build(self):
        # Création d'un ScreenManager pour gérer les transitions
        self.sm = ScreenManager()
        self.sm.add_widget(Fenetre_Principale(name='Fenetre_Principale'))
        self.sm.add_widget(Fenetre_Configuration(name='Fenetre_Configuration'))
        self.sm.add_widget(Fenetre_Categories(name='Fenetre_Categories'))
        self.sm.add_widget(Fenetre_Nouveau_Produit(name='Fenetre_Produits'))
        self.sm.add_widget(Fenetre_Suppression(name='Fenetre_Suppression'))
        return self.sm

    def appui_bouton(self, btn):
        print(btn.text, "POUR L'INSTANT CA FAIT RIEN")

if __name__ == '__main__':
    CaisseApp().run()
