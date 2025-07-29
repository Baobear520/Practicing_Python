
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def get_product_info(self):
        return f"Product(id: {self.id}, name: {self.name}, price: {self.price})"

    def __str__(self):
        return self.get_product_info()


class Order:
    def __init__(self):
        self._products = {}
        self.total_cost = 0

    def add_product(self, product: Product, quantity: int):
        old_quantity = self._products.get(product,0)
        self._products.update({product: old_quantity + quantity})
        self.update_total_cost(product,quantity, "add")

    def delete_product(self, product: Product, quantity: int):
        old_quantity = self._products.get(product)
        try:
            if old_quantity < quantity:
                raise ValueError
            self._products.update({product: old_quantity - quantity})
            self.update_total_cost(product,quantity,"remove")
        except ValueError:
            print(f"You cannot delete more than {old_quantity}")
        except Exception as e:
            print(f"{type(e).__name__} occured")


    def update_total_cost(self, product, quantity, action):
        if action == "add":
            self.total_cost = self.total_cost + product.price * quantity
        elif action == "remove":
            self.total_cost = self.total_cost - product.price * quantity

    def get_products_repr(self):
        return {k.name: v for k, v in self._products.items()}

    def get_order_info(self):
        return f"Order(products: {self.get_products_repr()}, total cost: {self.total_cost})"


banana = Product(1,"banana",5.5)
apple = Product(2,"red apple", 7.6)

order = Order()
order.add_product(banana, 5)
order.add_product(apple,10)
print(order.get_order_info())
order.delete_product(banana,6)
print(order.get_order_info())














