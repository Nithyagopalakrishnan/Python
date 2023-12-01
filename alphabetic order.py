a=[]
n=int(input("Enter the limit"))
for j in range(0,n):
	m=input("Enter the names")
	a.append(m)
a.sort()
print("Sorted String:")
for i in a:
    print(i)
