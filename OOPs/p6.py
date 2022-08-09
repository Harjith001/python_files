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
    #static method does not send any arguments by default unlike class methods
    @staticmethod
    def is_integer(num):
        #default method to check whether the given number is an instance of a data type
        if isinstance(num ,int):
            return True
        else:
            return False

    def __repr__(self):
        return f"Item({self.name},{self.price}, {self.quantity})"


print(Item.is_integer(7))

'''Difference between static and class methods
   If you are doing a work without interfering with instances
   like just checking a number is integer or not then use Static methods
   If your work concerns with instances then use Class methods'''

'''Static methods don't need self or cls to be passed as argument
   Whereas class methods need cls to be passed'''