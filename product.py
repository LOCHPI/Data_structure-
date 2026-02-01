class Product:
    def __init__(self, id, name, price, category, rating, sales):
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.rating = rating
        self.sales = sales

    def __str__(self):
        return f"{self.id} | {self.name} | {self.price} | {self.category} | {self.rating} | {self.sales}"
