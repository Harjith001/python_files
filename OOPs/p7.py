import csv


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

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def discount(self):
        self.price = self.price * self.pay_rate

    @classmethod
    def instantiate_from_csv(cls):
        with open("items.csv", 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=float(item.get('quantity'))
            )

    # static method does not send any arguments by default unlike class methods
    @staticmethod
    def is_integer(num):
        # default method to check whether the given number is an instance of a data type
        if isinstance(num, int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name},{self.price}, {self.quantity})"


class Phone(Item):  # sub_class(super_class)
    all = []

    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        # call to super function to access all attributes and methods
        super().__init__(name, price, quantity)
        assert broken_phones >= 0, f"Broken phones has negative value"
        # again typing attribute initilization and assert condition of super class is tedious
        # that's where super keyword comes in
        self.broken_phones = broken_phones
        Phone.all.append(self)


# creating two new instances of the class Item
# but by creating a broken_phone attribute which will not be useful for other items
# so we can create a separate class and inherit attributes of Item class

phone1 = Phone("nothing1", 500, 5, 1)
# Methods of super class can be used by sub class
print(phone1.calculate_total_price())
phone2 = Phone("Iphone13", 1490, 5, 1)
print(Item.all)
print(Phone.all)
