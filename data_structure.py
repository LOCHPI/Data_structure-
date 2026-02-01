from logger import Logger
from recommendation import recommend_products

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
logger = Logger()


def add_product():
    pid = input("product id: ").strip()

    for p in products:
        if p.id == pid:
            print(f"product with id {pid} already exists")
            logger.log(f"[ADD] failed (duplicate id): {pid}")
            return

    name = input("product name: ").strip()

    try:
        price = float(input("product price: ").strip())
    except ValueError:
        print("Invalid price")
        logger.log(f"[ADD] failed (invalid price): {pid}")
        return

    category = input("product category: ").strip()

    products.append(Product(pid, name, price, category, 0.0, 0))
    print(f"product {pid} added successfully!")
    logger.log(f"[ADD] success: {pid}")


def save_logging(a):
    logging.append(a)


def pop_product():
    if not products:
        print("No product to remove")
        logger.log("[REMOVE] failed (empty list)")
        return

    pid = input("product id: ").strip()

    target_index = -1
    for i in range(len(products)):
        if products[i].id == pid:
            target_index = i
            break

    if target_index == -1:
        print("Product not found")
        logger.log(f"[REMOVE] failed (not found): {pid}")
        return

    products.pop(target_index)
    print(f"product {pid} removed successfully!")
    logger.log(f"[REMOVE] success: {pid}")




def edit_product_inf():
    if not products:
        print("No product to edit")
        logger.log("[EDIT] failed (empty list)")
        return

    pid = input("product id: ").strip()

    target = None
    for p in products:
        if p.id == pid:
            target = p
            break

    if target is None:
        print("Product not found")
        logger.log(f"[EDIT] failed (not found): {pid}")
        return

    choice = input(
        "Select field:\n"
        "1) name\n"
        "2) price\n"
        "3) category\n"
        "4) rating\n"
        "5) sales\n"
        "choice: "
    ).strip()

    try:
        if choice == "1":
            target.name = input("new name: ").strip()
            logger.log(f"[EDIT] success (name): {pid}")

        elif choice == "2":
            target.price = float(input("new price: ").strip())
            logger.log(f"[EDIT] success (price): {pid}")

        elif choice == "3":
            target.category = input("new category: ").strip()
            logger.log(f"[EDIT] success (category): {pid}")

        elif choice == "4":
            target.rating = float(input("new rating: ").strip())
            logger.log(f"[EDIT] success (rating): {pid}")

        elif choice == "5":
            target.sales = int(input("new sales: ").strip())
            logger.log(f"[EDIT] success (sales): {pid}")

        else:
            print("Invalid choice")
            logger.log(f"[EDIT] failed (invalid choice): {pid}")
            return

        print("Done.")

    except ValueError:
        print("Invalid value")
        logger.log(f"[EDIT] failed (invalid value): {pid}")

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
     logger.log("[SEARCH] by name")
   



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
    logger.log("[SEARCH] by category")


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
    logger.log("[SEARCH] by price range")


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
    logger.log("[SORT] by price")


def sort_by_rating():
    if not products:
        print("No product to sort")
        save_logging("Sort by rating failed")

    for i in range(len(products)):
        for j in range(len(products)-i-1):
            if products[j].rating < products[j+1].rating:
                products[j], products[j+1] = products[j+1], products[j]

    save_logging("Sort by rating succeeded")
    logger.log("[SORT] by rating")


def sort_by_sales():
    if not products:
        print("No product to sort")
        save_logging("Sort by sales failed")

    for i in range(len(products)):
        for j in range(len(products)-i-1):
            if products[j].sales < products[j+1].sales:
                products[j], products[j+1] = products[j+1], products[j]

    save_logging("Sort by sales succeeded")
    def view_product_and_recommend():
    if not products:
        print("No products.")
        logger.log("[VIEW] failed (empty list)")
        return

    pid = input("Enter product id to view: ").strip()

    found = None
    for p in products:
        if p.id == pid:
            found = p
            break

    if found is None:
        print("Product not found")
        logger.log(f"[VIEW] failed (not found): {pid}")
        return

    logger.log(f"[VIEW] viewed: {found.id}")

    found.show_product_inf()

    recs = recommend_products(products, found, k=5, price_percent=0.2)

    print("\n--- Recommended ---")
    if len(recs) == 0:
        print("No recommendations.")
        logger.log(f"[RECOMMEND] none for id={found.id}")
    else:
        logger.log(f"[RECOMMEND] {len(recs)} items for id={found.id}")
        for r in recs:
            print(f"- {r.name} | {r.category} | {r.price} | id={r.id}")
    logger.log("[SORT] by sales")
def main():
    while True:
        print("\n1) Add product")
        print("2) Remove product")
        print("3) Edit product")
        print("4) Show product list")
        print("5) View product (and recommend)")
        print("0) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            add_product()
        elif choice == "2":
            pop_product()
        elif choice == "3":
            edit_product_inf()
        elif choice == "4":
            show_product_list()
        elif choice == "5":
            view_product_and_recommend()
        elif choice == "0":
            logger.log("[EXIT]")
            logger.print_logs()
            # logger.save_to_file("log.txt")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()




###   suggest product   ###





###   logging   ###

