from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button


# Gestion d'import des différentes fenêtres
class Fenetre_Principale(Screen):
    pass

class Fenetre_Configuration(Screen):
    pass

class Fenetre_Produits(Screen):
    pass

class Fenetre_Categories(Screen):
    pass

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
        self.sm.add_widget(Fenetre_Produits(name='Fenetre_Produits'))
        self.sm.add_widget(Fenetre_Suppression(name='Fenetre_Suppression'))
        
        return self.sm

    def updateCategories(self):
        self.fen = Fenetre_Principale()
        print(self.fen.ids.label_test.text)

        self.fen.ids.label_test.text = "OKOKOK"
        print(self.fen.ids.label_test.text)

    def appui_bouton(self, btn):
        print(btn.text)

if __name__ == '__main__':
    CaisseApp().run()
