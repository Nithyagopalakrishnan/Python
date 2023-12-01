def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
num=int(input("enter the limit"))
if num==0:
	print("factorial of 0 is 1")
else:
	result=fact(num)
	print("factorial of",num,"is",result)
