class Item:
    def __init__(self, name, price,
                 quantity=0):  # this method is like constructor in java.this method is executed automatically when an instance is created
        # by making quantity = 0 that means giving a default value when u don't the value currently
        # so if quantity is not passed then it will assume qunatity as 0 by default and show no error

        print(f"Instance is created : {name}")
        self.name = name  # here an attribute is created by passing argument value while creating an instance by using init() method
        self.price = price  # dynamicly allocating the attributes
        self.quantity = quantity

    # instead of passing separate variables to this function we can use self.attributes as it is already initialize
    # since we are passing self so it will also pass attributes connected to it
    def calculate_total_price(self):
        return self.price * self.quantity


'''instead of hardcoding attributes to avoid it 
   __init__(self) function is used'''
item1 = Item("Phone", 55900, 5)

print(item1.name, item1.price, item1.quantity)
print("Total price:", item1.calculate_total_price())

item2 = Item("Laptop", 129900, 3)
print(item2.name, item2.price, item2.quantity)
print("Total price:", item2.calculate_total_price())

# this is an attribute for this instance only item2 and other instances will not have this attribute
item2.has_numpad = False
# what if it would have been easier instead of declaring instances like above
# an instance can be created only by passing those attributes values
