from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.label import Label

class Fenetre_Principale(Widget,App):
    def __init__(self, **kwargs):
        super(Fenetre_Principale, self).__init__(**kwargs)

    def changeLabel(self):
        if self.ids.btn_test.text == "LOLOLOL":
            self.ids.btn_test.text = "LALA"
        else:
            self.ids.btn_test.text = "LOLOLOL"

class TestApp(App):
    def build(self):
        return Fenetre_Principale()
TestApp().run()