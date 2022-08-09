#practice - creating a oop structure

class footwear:
	def __init__(self,company:str,product_no:int,price:int,quantity=0):
		self.company = company
		self.product_no = product_no
		self.quantity = quantity
		self.price = price

	def total(self):
		return self.price*self.quantity

air_jordan = footwear("Nike",1,7,9990)
print(air_jordan.company,air_jordan.product_no,air_jordan.quantity,air_jordan.price)
print("Price of the product :",air_jordan.total())


