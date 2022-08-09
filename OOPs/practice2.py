class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, number_served = 0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = number_served

    def describe_restaurant(self):
        print(f'Restaurant Name : {self.restaurant_name}')
        print(f'Cuisine Type : {self.cuisine_type}')

    @staticmethod
    def open_restaurant():
        print('Restaurant is open')

    def increment_number_served(self,n):
        self.number_served += n


class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name, cuisine_type,number_served, flavours):
        super().__init__(restaurant_name, cuisine_type, number_served)
        self.flavours = flavours

    def display_flavours(self):
        print(self.flavours)


restaurant1 = Restaurant('Amsavalli Bhavan', 'Chettinad')
restaurant2 = Restaurant('Street Arabia', 'Arabian')
restaurant3 = Restaurant('Kumar Mess', 'Chettinad')

print(restaurant1.restaurant_name)
print(restaurant1.cuisine_type)
print(restaurant2.restaurant_name)
print(restaurant2.cuisine_type)
print(restaurant3.restaurant_name)
print(restaurant3.cuisine_type)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

Restaurant.open_restaurant()

restaurant = Restaurant('Chandran Mess','Chettinad', 69)
print(f'No. customers served by {restaurant.restaurant_name} = {restaurant.number_served}')

restaurant.increment_number_served(20)
print(f'No. customers served by {restaurant.restaurant_name} = {restaurant.number_served}')

flavours = ['vanilla','black current','butterscotch']
icecreamstand1 = IceCreamStand('Ibaco','Ice Cream',12,flavours)
icecreamstand1.describe_restaurant()
icecreamstand1.display_flavours()