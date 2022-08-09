class Item:
	def calculate_total_price(self,x ,y):
		return x*y

	'''self is used because in python the object itself is passed to the method as first parameter
		in python the methods has to receive atleast one parameter'''


item1 = Item() #creating an instance of a class item so item1 is an object of class Item
item1.name = "Phone" #creating attributes
item1.price = 55900
item1.quantity = 5
print("Total price of phones :",(item1.calculate_total_price(item1.price,item1.quantity)))

item2 = Item() #creating a new item2 instance of a class item
item2.name = "Laptop" #creating attributes
item2.price = 199900
item2.quantity = 5
print("Total price of laptops :",(item2.calculate_total_price(item2.price,item2.quantity)))
#creating a class compare it to creating a new data type and how a variable can be instancc\e of a data type

print(type(item1)) # __main__.Item like a data type
print(type(item1.name)) #str
print(type(item1.price)) #int
print(type(item1.quantity)) #int


s = "volla" #creating an instance of a string data type
print(s.upper()) #using methods from string class we are able to use it with instances

