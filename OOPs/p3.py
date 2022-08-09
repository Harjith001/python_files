class Item:
	#if u need to pass only specified datatypes into a variable the use variable: datatype
	#if u need to have some attributes as global like sale which has to applied to all instances
	#use class attributes so far used instance attributes

	pay_rate = 0.8 #rate after twenty percent discount

	def __init__(self,name : str,price : float,quantity = 0): 
		print(f"Instance is created : {name}")
		#checking some condition on passed arguments
		#assert is a keyword used to run some conditions on passed arguments the passed arguments 
		assert price>0, f"Price not greater than zero {price}"
		assert quantity>=0, f"Quantity not greater than or equal to zero {quantity}"

		#assigning values to self object
		self.name = name
		self.price = price 
		self.quantity = quantity

	def calculate_total_price(self):  
		return self.price * self.quantity

	def discount(self):
		self.price = self.price * self.pay_rate

item1 = Item("Phone",55900,5)  

print(item1.name,item1.price,item1.quantity)

item2 = Item("Laptop",129900,3)
print(item2.name,item2.price,item2.quantity)

#accessing class attributes
#these can be accessed by class name or even instances
print(Item.pay_rate)
print(item1.pay_rate) 
print(item2.pay_rate)

# __dict__ is a magic attribute: shows all attributes attached to that object
print(Item.__dict__) #class attributes
print(item1.__dict__) #instance attributes
 
#this __dict__ attribute converts all attributes and puts into a dictionary and returns is

#applying discount 
item1.discount()
#now item1.price will be changed after using the discount() method
print(item1.price)

#if you need to have different discount for a particular product then u can initialize it with instance attribute
item2.pay_rate = 0.7 #applying 30 percent discount for laptop alone now
item2.discount()
print(item2.price)

'''You can change value of a class attribute in instance level also. If the value is not changed 
   then it will have the same value as class attribute'''