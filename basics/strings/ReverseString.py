string="madanapalli"
s=" Andhrapradesh"
# using for loop
str=""
for elem in string:
    str=elem+str

print(str)

## using slicing
print(string[-1::-1])

## String concatenation
print(string+s)

## Repeating String
print((string+",")*2)
print("Hello "*3)

m="madanapalli"
n="Madanapalli"
print(m==n)
print("These two string are equal",m.casefold()==n.casefold())





