a=[]
n=int(input("enter the limit: "))
for j in range(0,n):
	m=input("enter the element: ")
	a.append(m)
temp=a[0]
max=len(a[0])
for i in a:
	if max<len(i):
		max=len(i)
		temp=len(i)
print("Length of longest word ",i,"is",temp)
