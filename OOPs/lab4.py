class Fraction:
	def __init__(self,num=1,den=1):
		self.num = num
		self.den = den
	def str(self):
		print(f"{self.num}/{self.den}")

	@staticmethod
	def add(self,other):
		f = Fraction()
		f.num = ((self.num*other.den)+(other.num *self.den))
		f.den = ((self.den * other.den))
		return f
	def sub(self,other):
		s = Fraction()
		s.num = ((self.num*other.den)-(other.num *self.den))
		s.den =((self.den * other.den))
		return s
	def mul(self,other):
		m = Fraction()
		m.num = ((self.num * other.num))
		m.den = ((self.den*other.den))
		rturn m
	def div(self,other):
		d = Fraction()
		d.num = (self.num * other.den)
		d.den = (self.den * other.num)
		return d

o1 = Fraction(2.0,3.0)
o2 = Fraction(4.0,5.0)

Fraction.add(o1,o2).str()
Fraction.sub(o1,o2).str()
Fraction.mul(o1,o2).str()
Fraction.div(o1,o2).str()

