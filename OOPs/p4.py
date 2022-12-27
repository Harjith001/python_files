class Item:
    pay_rate = 0.8
    all = []

    def __init__(self, name: str, price: float, quantity=0):
        print(f"Instance is created : {name}")
        assert price > 0, f"Price not greater than zero {price}"
        assert quantity >= 0, f"Quantity not greater than or equal to zero {quantity}"

        self.name = name
        self.price = price
        self.quantity = quantity

        # actions to execute
        # calling a class object and adding all instances to it

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):  # this magic method is used to represent an object with some name instead of location
        return f"Item({self.name},{self.price}, {self.quantity})"


item1 = Item("Phone", 55900, 5)
item2 = Item("Laptop", 129900, 3)
item3 = Item("Cable", 99, 5)
item4 = Item("Mouse", 490, 5)
item5 = Item("Keyboard", 1099, 5)

print(Item.all)  # list with five instances

# this is extremely usefull when u need to access all instance elements using loops
for instance in Item.all:
    print(instance.name)
