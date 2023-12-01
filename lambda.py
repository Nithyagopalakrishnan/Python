print("Rectangle...............")
print("\n")
l=int(input("Enter the length of rectangle: "))
b=int(input("Enter the breadth of rectangle: "))
area=lambda l,b: l*b
print("Area of the rectangle=",area(l,b))
perimeter=lambda l,b: 2*(l+b)
print("Perimeter of the rectangle=",perimeter(l,b))
print("\n")
print("Square.................")
print("\n")
a=int(input("Enter the length of one side"))
area=lambda a:a*a
print("Area of the Square=",area(a))
perimeter=lambda a:4*a
print("Perimeter of the Square",perimeter(a))
