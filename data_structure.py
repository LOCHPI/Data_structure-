import json
from logger import Logger
from recommendation import recommend_products


class Product:
    def __init__(self, id, name, price, category, rating, sales):
        self.id = id
        self.name = name
        self.price = float(price)
        self.category = category
        self.rating = float(rating)
        self.sales = int(sales)

    def __str__(self):
        return f"{self.id} | {self.name} | {self.price} | {self.category} | {self.rating} | {self.sales}"

    def show_product_inf(self):
        print(
            f"\n"
            f"id: {self.id}\n"
            f"name: {self.name}\n"
            f"price: {self.price}\n"
            f"category: {self.category}\n"
            f"rating: {self.rating}\n"
            f"sales: {self.sales}\n"
        )


products = []
logger = Logger()


def load_products_from_file(filename="data.json"):
    global products
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            products = []
            for item in data:
                products.append(
                    Product(
                        item["id"],
                        item["name"],
                        item["price"],
                        item["category"],
                        item.get("rating", 0.0),
                        item.get("sales", 0),
                    )
                )
    except FileNotFoundError:
        products = []
    except json.JSONDecodeError:
        products = []


def save_products_to_file(filename="data.json"):
    data = []
    for p in products:
        data.append(
            {
                "id": p.id,
                "name": p.name,
                "price": p.price,
                "category": p.category,
                "rating": p.rating,
                "sales": p.sales,
            }
        )

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


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
    save_products_to_file()
    print(f"product {pid} added successfully!")
    logger.log(f"[ADD] success: {pid}")


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
    save_products_to_file()
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

        save_products_to_file()
        print("Done.")

    except ValueError:
        print("Invalid value")
        logger.log(f"[EDIT] failed (invalid value): {pid}")


def show_product_list():
    if not products:
        print("No product to show")
        return

    for i, p in enumerate(products, 1):
        print(f"{i}.")
        p.show_product_inf()


def search_by_name():
    if not products:
        print("No product to search")
        logger.log("[SEARCH] by name (empty list)")
        return

    a = input("Enter product name: ").strip().lower()
    result = False

    for p in products:
        if p.name.strip().lower() == a:
            p.show_product_inf()
            result = True

    if not result:
        print(f"Product with name {a} not found!")

    logger.log("[SEARCH] by name")


def search_by_category():
    if not products:
        print("No product to search")
        logger.log("[SEARCH] by category (empty list)")
        return

    a = input("Enter product category: ").strip().lower()
    result = False

    for p in products:
        if p.category.strip().lower() == a:
            p.show_product_inf()
            result = True

    if not result:
        print(f"Product with category {a} not found!")

    logger.log("[SEARCH] by category")


def search_by_price_range():
    if not products:
        print("No product to search")
        logger.log("[SEARCH] by price range (empty list)")
        return

    try:
        max_p = float(input("Product max price: ").strip())
        min_p = float(input("Product min price: ").strip())
    except ValueError:
        print("Invalid price range")
        logger.log("[SEARCH] by price range (invalid input)")
        return

    if min_p > max_p:
        min_p, max_p = max_p, min_p

    result = []
    for p in products:
        if min_p <= p.price <= max_p:
            result.append(p)

    if not result:
        print("No product found in this range")
        logger.log("[SEARCH] by price range (no results)")
        return

    for j, m in enumerate(result, 1):
        print(f"{j}.")
        m.show_product_inf()

    logger.log("[SEARCH] by price range")


def sort_by_price(ascending=True):
    if not products:
        print("No product to sort")
        logger.log("[SORT] by price (empty list)")
        return

    n = len(products)
    for i in range(n):
        for j in range(n - i - 1):
            if ascending:
                if products[j].price > products[j + 1].price:
                    products[j], products[j + 1] = products[j + 1], products[j]
            else:
                if products[j].price < products[j + 1].price:
                    products[j], products[j + 1] = products[j + 1], products[j]

    logger.log("[SORT] by price")


def sort_by_rating():
    if not products:
        print("No product to sort")
        logger.log("[SORT] by rating (empty list)")
        return

    n = len(products)
    for i in range(n):
        for j in range(n - i - 1):
            if products[j].rating < products[j + 1].rating:
                products[j], products[j + 1] = products[j + 1], products[j]

    logger.log("[SORT] by rating")


def sort_by_sales():
    if not products:
        print("No product to sort")
        logger.log("[SORT] by sales (empty list)")
        return

    n = len(products)
    for i in range(n):
        for j in range(n - i - 1):
            if products[j].sales < products[j + 1].sales:
                products[j], products[j + 1] = products[j + 1], products[j]

    logger.log("[SORT] by sales")


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


def main():
    load_products_from_file()

    while True:
        print("\n1) Add product")
        print("2) Remove product")
        print("3) Edit product")
        print("4) Show product list")
        print("5) Search by name")
        print("6) Search by category")
        print("7) Search by price range")
        print("8) Sort by price (asc)")
        print("9) Sort by price (desc)")
        print("10) Sort by rating (desc)")
        print("11) Sort by sales (desc)")
        print("12) View product (and recommend)")
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
            search_by_name()
        elif choice == "6":
            search_by_category()
        elif choice == "7":
            search_by_price_range()
        elif choice == "8":
            sort_by_price(True)
        elif choice == "9":
            sort_by_price(False)
        elif choice == "10":
            sort_by_rating()
        elif choice == "11":
            sort_by_sales()
        elif choice == "12":
            view_product_and_recommend()
        elif choice == "0":
            logger.log("[EXIT]")
            save_products_to_file()
            logger.print_logs()
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
