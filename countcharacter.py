n=input("enter the string")
count=0
for i in range(len(n)):
	if n[i]!=' ':
		count=count+1
print("number of characters in the string are:",count)
