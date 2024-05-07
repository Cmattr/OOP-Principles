'''Task 1: Create Base Product Class

Develop a base class Product with common attributes like product ID, name, price, and a method to display product information.
Expected Outcome: A Product class that can hold general information about a product and display it.

Task 2: Implement Subclasses for Specific Products

Create subclasses Book, Electronic, and Clothing that inherit from Product.
Each subclass should have additional attributes relevant to its category (e.g., author for books, specs for electronics, size for clothing).
Expected Outcome: Each subclass contains both inherited attributes from Product and new attributes specific to the product type.

Task 3: Override Display Method in Subclasses

Override the method to display product information in each subclass to include specific attributes.
For example, the Book class should display the author, Electronic should display specs, etc.
Expected Outcome: Calling the display method on an instance of any subclass shows both common and specific product details.

Task 4: Test Product Catalog Functionality

Instantiate objects of each subclass and call their display methods to ensure correct information is shown.
Expected Outcome: The system should accurately display detailed information for each type of product, demonstrating inheritance and method overriding.'''

#Task 1: Create Base Product Class
class Base:
    def __init__(self, product_id, name, price):
        self._product_id = product_id
        self.name = name
        self._price = price
    
    def get_product_id(self):
        return self._product_id
    
    def get_price(self):
        return self._price
    
    def set_product_id(self, new_id):
        self._product_id = new_id 
    
    def set_price(self, new_price):
        self._price = new_price
    
    
    def display_product(self):
        print (f"product name: {self.name}")
        print(f"product ID: {self.get_product_id()}")
        print(f"product price: ${self.get_price()}")  

#Task 2: Implement Subclasses for Specific Products
class Book(Base):
    def __init__(self, product_id, name, price, author):
        super().__init__(product_id, name, price)
        self.author = author

    # Task 3: Override Display Method in Subclasses
    def display_product(self):
        print("\n Category: Book")
        print (f"nproduct name: {self.name}")
        print(f"product ID: {self.get_product_id()}")
        print(f"product price: ${self.get_price()}")  
        print(f"Author: {self.author}\n")


class Electronics(Base):
    def __init__(self, product_id, name, price, specs):
        super().__init__(product_id, name, price)
        self.specs = specs
    
    # Task 3: Override Display Method in Subclasses
    def display_product(self):
        print("\n Category: Electronics")
        print (f"product name: {self.name}")
        print(f"product ID: {self.get_product_id()}")
        print(f"product price: ${self.get_price()}")  
        print(f"Author: {self.specs}\n")

class Clothing(Base):
    def __init__(self, product_id, name, price, size):
        super().__init__(product_id, name, price)
        self.size = size
    # Task 3: Override Display Method in Subclasses
    def display_product(self):
        print("\n Category: Clothing")
        print (f"product name: {self.name}")
        print(f"product ID: {self.get_product_id()}")
        print(f"product price: ${self.get_price()}")  
        print(f"Author: {self.size}\n")


# Task 4: Test Product Catalog Functionality
hardcover = Book("1234", "The Hobbit", 30, "J.R.R Tolkien")
hardcover.display_product()

tv = Electronics("5678", "Samsung Smart TV", 350, "1080p" )
tv.display_product()

shirt = Clothing("9123", "Graphic T-Shirt", 15, "XL")
shirt.display_product()