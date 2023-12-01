def fib(n):
	c=0
	if n==0 or n==1:
		return n
	else:
		c=fib(n-1)+fib(n-2)
		return c
a=int(input("enter the range"))
for i in range(0,a):
	print(fib(i))
