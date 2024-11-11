from kivy.storage.jsonstore import JsonStore

class JsonStoreDatabase:
    def __init__(self, filepath='database.json'):
        self.store = JsonStore(filepath)
        if not self.store.exists("categories"):
            self.store.put("categories", noms=[])
        if not self.store.exists("produits"):
            self.store.put("produits", items=[])

    def add_category(self, category_name):
        """Ajoute une nouvelle catégorie si elle n'existe pas déjà."""
        categories = self.store.get("categories")["noms"]
        if category_name not in categories:
            categories.append(category_name)
            self.store.put("categories", noms=categories)

    def add_product(self, product_name, category_name, price):
        """Ajoute un produit avec nom, catégorie et prix spécifiés."""
        categories = self.store.get("categories")["noms"]
        if category_name not in categories:
            raise ValueError(f"La catégorie '{category_name}' n'existe pas.")
        
        new_product = {
            "nom": product_name,
            "categorie": category_name,
            "prix": str(price)
        }
        produits = self.store.get("produits")["items"]
        produits.append(new_product)
        self.store.put("produits", items=produits)

    def get_products_by_category(self, category_name):
        """Retourne une liste de produits appartenant à une catégorie donnée."""
        produits = self.store.get("produits")["items"]
        return [product for product in produits if product["categorie"] == category_name]

    def update_product_price(self, product_name, new_price):
        """Met à jour le prix d'un produit spécifié."""
        produits = self.store.get("produits")["items"]
        for product in produits:
            if product["nom"] == product_name:
                product["prix"] = str(new_price)
                self.store.put("produits", items=produits)
                return
        raise ValueError(f"Le produit '{product_name}' n'existe pas.")

    def delete_product(self, product_name):
        """Supprime un produit par son nom."""
        produits = self.store.get("produits")["items"]
        produits = [product for product in produits if product["nom"] != product_name]
        self.store.put("produits", items=produits)

    def delete_category(self, category_name):
        """Supprime une catégorie et tous les produits associés."""
        categories = self.store.get("categories")["noms"]
        if category_name in categories:
            categories.remove(category_name)
            produits = self.store.get("produits")["items"]
            produits = [product for product in produits if product["categorie"] != category_name]
            self.store.put("categories", noms=categories)
            self.store.put("produits", items=produits)
        else:
            raise ValueError(f"La catégorie '{category_name}' n'existe pas.")

    def get_all_categories(self):
        """Retourne la liste de toutes les catégories."""
        return self.store.get("categories")["noms"]

    def get_all_products(self):
        """Retourne la liste de tous les produits."""
        return self.store.get("produits")["items"]
