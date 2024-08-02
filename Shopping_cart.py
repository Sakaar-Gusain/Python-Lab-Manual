class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"Product ID: {self.id}, Name: {self.name}, Price: ${self.price}, Stock: {self.stock}"

class Customer:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.email = email  

class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, product, quantity):
        if product.id in self.items:
            self.items[product.id] += quantity
        else:
            self.items[product.id] = quantity

    def remove_item(self, product, quantity):
        if product.id in self.items:
            self.items[product.id] -= quantity
            if self.items[product.id] <= 0:
                del self.items[product.id]

    def calculate_total(self, products):
        total = 0
        for product_id, quantity in self.items.items():
            product = products[product_id]
            total += product.price * quantity
        return total

class Order:
    def __init__(self, customer, cart, total):
        self.customer = customer
        self.cart = cart
        self.total = total

    def process_order(self, products):
        for product_id, quantity in self.cart.items.items():
            product = products[product_id]
            if product.stock < quantity:
                print(f"Error: Insufficient stock for product '{product.name}'")
                return False
        for product_id, quantity in self.cart.items.items():
            product = products[product_id]
            product.stock -= quantity
        print("Order processed successfully")
        return True

# Example usage:

# Create products
products = {
    1: Product(1, "Phone", 500, 10),
    2: Product(2, "Laptop", 1000, 5),
    3: Product(3, "Headphones", 100, 20)
}

# Create customer
customer = Customer(1, "Alice", "alice@example.com")

# Create shopping cart
cart = ShoppingCart()

# Add items to the cart
cart.add_item(products[1], 2)
cart.add_item(products[2], 1)

# Remove items from the cart
cart.remove_item(products[1], 1)

# Calculate total
total = cart.calculate_total(products)

# Create order
order = Order(customer, cart, total)

# Process order
order.process_order(products)

# Print remaining stock
for product_id, product in products.items():
    print(product)