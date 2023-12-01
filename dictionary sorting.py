student={}
n=int(input("enter the limit"))
for i in range(0,n):
	name=input("Enter the Name : ")
	age=int(input("Enter the Age : "))
	grade=input("Enter the Grade : ")
	student[name]=age,grade
print(student)
li=list(student.items())
li.sort()
print("Ascending order is",li)
li.sort(reverse=True)
print("Descending order is",li)
