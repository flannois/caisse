import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

# Classe pour la page d'accueil avec les catégories et les produits
class AccueilScreen(Screen):
    category_label = StringProperty("Catégorie")
    products_layout = ObjectProperty()

    def on_pre_enter(self):
        self.update_category("biere")  # Afficher une catégorie par défaut

    def update_category(self, category_name):
        self.category_label = category_name.capitalize()
        self.products_layout.clear_widgets()

        # Exemple de produits par catégorie, à remplacer par un système dynamique
        products = {
            "biere": ["Pale Ale", "IPA", "Stout"],
            "vin": ["Merlot", "Chardonnay", "Pinot Noir"]
        }
        for product in products.get(category_name, []):
            self.products_layout.add_widget(ProductButton(text=product))

# Classe pour gérer les catégories
class CategoriesScreen(Screen):
    pass

# Classe pour gérer les produits
class ProductButton(BoxLayout):
    text = StringProperty()

# Gestionnaire d'écran
class CaisseApp(App):
    def build(self):
        return ScreenManager()

if __name__ == "__main__":
    CaisseApp().run()
