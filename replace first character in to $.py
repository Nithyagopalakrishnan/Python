string=input("enter the string: ")
char=string[0]
new_string=char+string[1:].replace(char,'$')
print("the replaced string is ",new_string)
