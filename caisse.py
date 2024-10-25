from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget

# Gestion d'import des différentes fenêtres
class Fenetre_Principale(Screen):
    def __init__(self, **kwargs):
        super(Fenetre_Principale, self).__init__(**kwargs)

    def updateCategories(self):
        print(self.ids)
        if self.ids.label_test.text == "LOLOLOL":
            self.ids.label_test.text = "LALA"
        else:
            self.ids.label_test.text = "LOLOLOL"

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
        print(self.sm.ids)
        return self.sm

    def appui_bouton(self, btn):
        print(btn.text)

if __name__ == '__main__':
    CaisseApp().run()
