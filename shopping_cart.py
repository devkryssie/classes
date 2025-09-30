class shoppingcart:
    def __init__(self):
        self.items = {}
    def add_item(self, item , price, quantity=1):
        if item in self.items:
            self.items[item]["quantity"] += quantity
        else:
            self.items[item] = {"price": price, "quantity": quantity}
    def remove_item(self, item, quantity=1):
        if item in self.items:
            if self.items[item]["quantity"] > quantity:
                self.items[item]["quantity"] -= quantity
            else:
                del self.items[item]
    def clear_cart(self):
        self.items.clear()
    def calculate_total(self):
        total = 0
        for details in self.items.values():
            total += details["price"] * details["quantity"]
        return total
cart = shoppingcart()
cart.add_item("shirt", 200, 3)
cart.add_item("apple", 100, 2)
print("total =", cart.calculate_total())


