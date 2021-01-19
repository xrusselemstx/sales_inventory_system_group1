
def log_in():
    user_name = input("Please enter your username: ")
    user_pw = input("Please enter your password: ")
    # two types of log in:
    # 1) admin/staff user (closed for new accounts)
    # 2) customers (open for new accounts)

def register():
    # sign up/new account for customers

class Product:
    def __init__(self, prod_name, prod_price, prod_qntty):
        self.prod_name = prod_name
        self.prod_price = prod_price
        self.prod_qntty = prod_qntty

    def add_product():
        # adds a new product to the inventory system
        pass

    def del_product():
        # deletes a product from the inventory system
        pass

    def view_product():
        # two options:
        # displays the complete sorted list of products from the inventory system
        # displays 1 product with info. from the inventory system
        pass

    def upd_product():
        # updates an old product in the inventory system
        pass

    def search_product():
        # returns a product if it is found in the inventory system
        pass

    def sales_product():
        # records sales history of products in the inventory system
        pass

class Admin(Product):
    # inherits the Product class
    pass

class Customer:
    def __init__(self, customer_info):
        # TODO:
        pass

    def add_to_cart():
        # TODO:
        pass

    def view_cart():
        # TODO:
        pass

    def del_from_cart():
        # TODO:
        pass

    def check_out():
        # TODO:
        pass

    def view_products():
        # TODO:
        pass
