a=input("enter the string to be counted : ")
count=0
for i in range(len(a)):
	if a[i]=="a":
			count=count+1
print("number of 'a' in the given string is:",count)
