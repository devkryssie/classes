class bus:
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
    def add_passenger(self, name):
        if len(self.passengers) < self.capacity:
            self.passengers.append(name)
            print(f"{name} added to the bus")
        else:
            print("bus is full")
    def remove_passenger(self, name):
        if name in self.passengers:
            self.passengers.remove(name)
    def show_passenger(self):
        return self.passengers
metro_bus = bus(capacity=3)
metro_bus.add_passenger("john")
metro_bus.add_passenger("mary")
metro_bus.add_passenger("paul")
metro_bus.add_passenger("lisa")
print(metro_bus.show_passenger())

