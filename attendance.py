n=int(input("Enter the number of student: "))
a=int(input("Enter the number of present days: "))
s=[]
for i in range(0,n):
	name=input("Enter the Name of the student: ")
	attendance=int(input("Enter the Attendace: "))
	percentage=int((attendance/a)*100)
	s.append((percentage,name))
print("Attendance is",s)	
s.sort(reverse=True)
print("Descending order is")
for i in s:
	print(i)
