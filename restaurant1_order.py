import time
class Restaurant:
    def __init__(self, name, tables):
        self.name = name
        self.tables = tables
        self.orders = {}
        self.ready_foods = []
        self.cooking_times = {}
        print(f"welcome to {self.name} 😋😋\n")
        print(f"welcome to {self.name} good food is the foundation of genuine happiness😇")
    def set_cooking_time(self, food, seconds):
        self.cooking_times[food] = seconds
        print(f"cooking time for {food} set to {seconds} seconds please stay with us😉")
    def add_ready_food(self, food):
        if food not in self.ready_foods:
             self.ready_foods.append(food)
             print(f"{food} is now ready we dont waste time in {self.name}🤫")

    def place_order(self, table_number, food):
        if table_number not in self.tables:
            print("invalid table number")
            return
        if food not  in self.ready_foods:
            cook_time = self.cooking_times.get(food, 3)
            print(f"food {food} is on fire cooking in {cook_time} sec......please wait and stay calm🥱😮")
            time.sleep(cook_time)
            self.add_ready_food(food)
        if table_number not in self.orders:
            self.orders[table_number] = []
            self.orders[table_number].append(food)
            print(f"order placed: {food} at table {table_number}")
            print("thank you see u next time 🍳")
    def view_orders(Self, table_number):
        if table_number not in Self.orders:
            print("no orders for this table yet")
            return
        print(f"\norders for table {table_number}")
        for food in Self.orders[table_number]:
            print(f"{food}")
tables = [1,2,3,4]
restuarant = Restaurant("kryssie's foodie hub", tables)
restuarant.set_cooking_time("rice", 120)
restuarant.set_cooking_time("chicken", 5)
#restuarant.set_cooking_time("beans", 4)
restuarant.set_cooking_time("beef", 3)
restuarant.set_cooking_time("kunu", 3)
restuarant.add_ready_food("water")
restuarant.place_order(1, "water")
restuarant.place_order(2, "rice")
restuarant.place_order(3, "chicken")
restuarant.place_order(4, "beef")
#restuarant.place_order(5, "kunu")
restuarant.view_orders(1)
restuarant.view_orders(2)
restuarant.view_orders(3)
restuarant.view_orders(4)
#restuarant.view_orders(5)
