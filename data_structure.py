class Product:
    def __init__(self, id, name, price, category, rating, sales):
        self.id= id
        self.name = name
        self.price = price
        self.category = category
        self.rating = rating
        self.sales = sales

    def __str__(self):
        return f"{self.id} | {self.name} | {self.price} | {self.category} | {self.rating} | {self.sales}"


    def show_product_inf(self):
        print(f"""
              id: {self.id}
              name: {self.name}
              price: {self.price}
              category: {self.category}
              rating: {self.rating}
              sales: {self.sales}""")



####   product management   ###

products = []
logging = []


def add_product():
    id = input("product id: ")
    for p in products:
      if p.id == id:
         print(f"product with id {p.id} already exists")
         save_logging("Adding Product failed" + id)
         return

    name = input("product name: ")
    price = float(input("product price: "))
    category = input("product category: ")

    products.append(Product(id, name, price, category,rating=0, sales=0 ))
    print(f"product {id} added successfully!")
    save_logging("Adding Product succeeded" + id)


def save_logging(a):
    logging.append(a)


def pop_product():
    if not products:
        print("No product to pop")
        save_logging("Removing Product failed")
        return

    id = input("product id: ")
    for p in products:
        if p.id == id:
            products.remove(p)
            print(f"product {id} removed successfully!")
            save_logging("Removing Product failed" + id)
            return

    print("Product not found")
    save_logging("Removing Product failed" + id)



def edit_product_inf():
    if not products:
        print("No product to edit")
        save_logging("Editing Product failed")

    id = input("product id: ")
    for p in products:
        if p.id == id:
            choice = input(f"""
            Select the property you want to edit {p.id} :
             1. name
             2. price
             3. category
             4. rating
             5. sales
             6. id         
""")
            try:
              if choice == "1":
                a = input("Enter new value :")
                p.name = a
                print(f"Product name changed to {a}!")

              if choice == "2":
                a = input("Enter new value :")
                p.price = a
                print(f"Product price changed to {a}!")

              if choice == "3":
                a = input("Enter new value :")
                p.category = a
                print(f"Product category changed to {a}!")

              if choice == "4":
                a = input("Enter new value :")
                print(f"Product rating changed to {a}!")

              if choice == "5":
                a = input("Enter new value :")
                print(f"Product sales changed to {a}!")

              if choice == "6":
                a = input("Enter new value :")
                p.id = a
                print(f"Product id changed to {a}!")
              save_logging("Editing Product succeeded" + str(id))

            except ValueError:
                print("Invalid value")
                save_logging("Editing Product failed" + str(id))


def show_product_list():
    if not products:
        print("No product to show")

    for i , p in enumerate(products,1):
        print(f"{i}. ")
        p.show_product_inf()



###   search menu   ###


def search_by_name():
    if not products:
        print("No product to search")
        save_logging("Searching Product failed")
        return

    a = input("Enter product name :").strip().lower()
    result = False
    for p in products:
        if p.name.lower().strip() == a:
            p.show_product_inf()
            result = True
            save_logging("Search by name succeeded" + p.id)

    if not result:
        print(f"Product with name {a} not found !")
        save_logging("Search by name failed")



def search_by_category():
    if not products:
        print("No product to search")
        save_logging("Searching Product failed")
        return

    a = input("Enter product category :").strip().lower()
    result = False
    for p in products:
        if p.category.lower().strip() == a:
            p.show_product_inf()
            result = True
            save_logging("Search by category succeeded" + p.id)

    if not result:
        print(f"Product with category {a} not found !")
        save_logging("Search by category failed")



def search_by_price_range():
    if not products:
        print("No product to search")
        save_logging("Search by price range failed")

    result = []
    max_p = float(input("Product max price :"))
    min_p = float(input("Product min price :"))

    for p in products:
        if min_p <= p.price <= max_p :
            result.append(p)

    if not result:
        print("No product found in this range")
        save_logging("Search Product failed")

    for j , m in enumerate(result,1):
        print(f"{j}. {m.show_product_inf()}")

    save_logging("Search by price range succeeded")



###   To bubble sort products   ###


def sort_by_price(result = True):
    if not products:
        print("No product to sort")
        save_logging("Sort by price failed")
        return

    for i in range(len(products)):
        for j in range(len(products)-i-1):
          if result:
            if products[j].price > products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]

          else:
            if products[j].price < products[j+1].price:
                products[j], products[j+1] = products[j+1], products[j]

    save_logging("Sort by price succeeded")



def sort_by_rating():
    if not products:
        print("No product to sort")
        save_logging("Sort by rating failed")

    for i in range(len(products)):
        for j in range(len(products)-i-1):
            if products[j].rating < products[j+1].rating:
                products[j], products[j+1] = products[j+1], products[j]

    save_logging("Sort by rating succeeded")



def sort_by_sales():
    if not products:
        print("No product to sort")
        save_logging("Sort by sales failed")

    for i in range(len(products)):
        for j in range(len(products)-i-1):
            if products[j].sales < products[j+1].sales:
                products[j], products[j+1] = products[j+1], products[j]

    save_logging("Sort by sales succeeded")



###   suggest product   ###




###   logging   ###