from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label

class DropdownExample(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'

        # Label pour afficher l'option sélectionnée
        self.label = Label(text="Sélectionnez une option")
        self.add_widget(self.label)

        # Création du DropDown
        self.dropdown = DropDown()

        # Options à ajouter dans le DropDown
        options = ['Option 1', 'Option 2', 'Option 3']
        for option in options:
            btn = Button(text=option, size_hint_y=None, height=44)
            # Ajouter une action au clic
            btn.bind(on_release=lambda btn: self.select_option(btn.text))
            self.dropdown.add_widget(btn)

        # Bouton principal pour ouvrir le DropDown
        self.main_button = Button(text='Menu déroulant', size_hint=(None, None), size=(200, 44))
        self.main_button.bind(on_release=self.dropdown.open)
        self.add_widget(self.main_button)

    def select_option(self, option):
        self.label.text = f"Vous avez sélectionné : {option}"
        self.dropdown.dismiss()  # Fermer le menu déroulant

class DropdownApp(App):
    def build(self):
        return DropdownExample()

if __name__ == '__main__':
    DropdownApp().run()
