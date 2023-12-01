student={}
n=int(input("enter the limit"))
for i in range(0,n):
	name=input("Enter the Name : ")
	age=int(input("Enter the Age : "))
	grade=input("Enter the Grade : ")
	student[name]=age,grade
print(student)
