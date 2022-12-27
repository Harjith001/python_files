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

    # making ths as class method as we do not know which are the instances
    # to make a mthod a class method we have to use decorator
    # decorators are used to modify behavior of a function or a class

    # when we call a class method then cls - class reference is passed
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

    def __repr__(self):
        return f"Item({self.name},{self.price}, {self.quantity})"


# using a csv file to store and retrieve data
# csv - comma separated values
Item.instantiate_from_csv()  # when this function is called, instances for the class are created
print(Item.all)
