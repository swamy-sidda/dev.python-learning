

# slicing
li=[0,1,2,2,2,3,4,5,5,6,6,7,9,8,9,10]
l1=[10,20,30,40,50,60,70,80,90]


# li=li.extend(l1)
# print(f"list--> {li}")

# print(f"combining after--> {li.extend(l1)}")

# li=li.extend(l1)
# print(f"list--> {li}")

li.reverse()
print(f"list is ---> {li}")

li.sort()
print(f"list ascending order is ---> {li}")
li.sort(reverse=True)
print(f"list descending order is ---> {li}")
print(li)
print(f"first--> {li[0:len(li):2]}")
print(f"last--> {li[-1:-len(li):-2]}")

print(f"third--> {li[::]}")

print(f"fourth--> {li[:]}")

li.append(11)
print(f"list--> {li}")

li.insert(0,100)
print(f"list--> {li}")

li.remove(1)
print(f"list--> {li}")


print('--------------------------------------------------------------------------------')
l=[10,20,30,40,50,60,70,80,90,100]

for item in l:
    print(item)
print("----------------------------")
for i in range(0,10):
    print(l[i])


l=[10,20,30,40,50,60,70,80,90,100]
print(l,type(l))

print("--------------------------")

r=range(10)
print(r)
print(type(r))

print("--------------------------")

li=list(r)
print(li,type(li))

print("-----------------")

list=[]
print(list)
print(type(list))

