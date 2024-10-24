from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen

# Gestion d'import des différentes fenêtres
class Fenetre_Principale(Screen):
    pass

class Fenetre_Configuration(Screen):
    pass

class Fenetre_Produits(Screen):
    pass

class Fenetre_Categories(Screen):
    pass



# Gestionnaire d'écran
class CaisseApp(App):
    def build(self):
        # Création d'un ScreenManager pour gérer les transitions
        sm = ScreenManager()
        sm.add_widget(Fenetre_Principale(name='Fenetre_Principale'))
        sm.add_widget(Fenetre_Configuration(name='Fenetre_Configuration'))
        sm.add_widget(Fenetre_Categories(name='Fenetre_Categories'))
        sm.add_widget(Fenetre_Produits(name='Fenetre_Produits'))
        
        return sm

    def appui_bouton(self, btn):
        print(btn.text)

if __name__ == '__main__':
    CaisseApp().run()
