def add(a,b):
	c=a+b
	return c
def sub(a,b):
	c=a-b
	return c
def mul(a,b):
	c=a*b
	return c
def div(a,b):
	c=a/b
	return c
def power(a,b):
	c=a**b
	return c
m=int(input("enter the first number"))
n=int(input("enter the second number"))
print("OPERATIONS  1.+   2.-  3.*   4./  5.**")
choice=input("enter the choice")
if choice=="+":
	print("the result is",add(m,n))
elif choice=="-":
	print("the result is",sub(m,n))
elif choice=="*":
	print("the result is",mul(m,n))
elif choice=="/":
	print("the result is",div(m,n))
elif choice=="**":
	print("the result is",power(m,n))
else:
	print("invalid choice")
