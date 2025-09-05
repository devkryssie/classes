class shoppingcart:
    prices = {}
    cart = {}
    def setup_cart(prices):
        shoppingcart.prices = prices
        shoppingcart.cart = {}
    def add_item(self, item , quantity=1):
        if item in shoppingcart.prices:
            shopping.cart[item] = shopping.cart.get(item, 0) + quantity
    def remove_item(self, item, quantity=1):
        if item in self.cart:
            self.cart[item] -= quantity
            if self.cart[item] <= 0:
                del shopping.cart[item]
    def clear_cart():
        shoppingcart.cart.clear()
    def calculate_total():
        total = 0
        for item, quantity in shoppingcart.cart.items():
            total += shoppingcart.prices[item] * quantity
        return total
prices = {"shirt": 5000, "shoes": 12000}
shoppingcart.setup_cart(prices)
shoppingcart.add_item("shirt", 2)
print(shoppingcart.calculate_total())
shoppingcart.remove_item("shirt", 1)
print(shoppingcart.calculate_total())
