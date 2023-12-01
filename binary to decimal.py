n=int(input("enter the binary number"))
dec=0
rem=0
i=1
while n!=0:
	rem=n%10
	dec=dec+rem*i
	i=i*2
	n=int(n/10)
print("corresponding decimal value is",dec)
