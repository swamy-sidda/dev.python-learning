str='123456'
print(str[0:6:-1])

string="Python programming from Madanapalle"
print(string)
print(string[0:len(string):])
print(string[0:len(string):2])
print(string[0:len(string):3])
print(string[0:len(string):4])
print(string[0:len(string):5])

str=("madanapalli")
print(str[:len(str)])
print(f"{str[0:200:-1]}'str[0:200:-1]' is not print anything")
print(str[2:6:1])

print("starting point 1")
print(f"-----------------------------")
str=" and it is that it is and is it is was and is"
print(str,"--->",type(str),len(str))
print(str.find(" ",10,len(str)+1))

print(f"{str.replace("it","IT")} replace multiple ")

print(f"{str.index("and")}  --->")
print(f"count of 'is': {str.count("is")}")

string="gnanambica degree college"

print(string.replace("gnanambica","Shri Gnanambica"))
