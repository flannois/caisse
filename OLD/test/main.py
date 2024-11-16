from kivy.app import App
from kivy.lang import Builder
from kivy.uix.recycleview.views import RecycleDataViewBehavior
from kivy.uix.recycleview import RecycleView
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import StringProperty
import sqlite3

from BaseDeDonnees import BaseDeDonnees
bdd = BaseDeDonnees()



# Widget personnalisé pour chaque élément de la liste
class CategoryRow(BoxLayout, RecycleDataViewBehavior):
    text = StringProperty("")
    category_id = StringProperty("")

    def delete_item(self):
        bdd.supprimer_categorie(self.category_id)
        App.get_running_app().root.update_categories()


# RecycleView personnalisée
class CategoryRecycleView(RecycleView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.update_categories()

    def update_categories(self):
        categories = bdd.lister_categories()
        self.data = categories


# L'application principale
class CategoryApp(App):
    def build(self):
        return Builder.load_file("categories.kv")


if __name__ == "__main__":
    CategoryApp().run()
