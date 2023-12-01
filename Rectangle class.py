class rect:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
	def area(self):
		c=self.length*self.breadth
		print("Area of the Rectangle : ",c)
	def perimeter(self):
		p=2*(self.length+self.breadth)
		print("Perimeter of the Rectangle : ",p)
a=int(input("Enter the length of the Rectangle : "))
b=int(input("Enter the breadth of the Rectangle : "))
obj=rect(a,b)
obj.area()
obj.perimeter()
