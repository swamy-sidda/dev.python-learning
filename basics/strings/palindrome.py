str=str(input("enter a string to conclude that palindrome or not "))
str=str.lower()
if(str==str[::-1]):
    print("yes it's a palindrome ")
else:
    print("no it's not a palindrome ")

if(str=="".join(reversed(str))):
    print("yes it's a palindrome ")
else:
    print("no it's not a palindrome ")

str1=""
for i in str:
    str1=i+str1
if(str1==str):
    print("yes it's a palindrome ")
else:
    print("no it's not a palindrome ")