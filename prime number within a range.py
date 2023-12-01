u=int(input("enter the upper limit"))
l=int(input("enter the lower limit"))
print("prime numbers within a limit",l,"and",u,":")
for i in range(l,u):`
 if i==0 or i==1:
   continue
 j=2
 flag=0
 while j<=i/2:
    if i%j==0:
     flag=1
     break
    j=j+1
 if flag==0:
    print(i)  
