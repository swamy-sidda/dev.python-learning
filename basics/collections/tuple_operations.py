


tuple= (2,2,3,4,5,5,3,4,10,2)
print(f"tuple--> {tuple}")
print(f"tuple--> {1,2,3,4,5,6,7,8}")

print(f"count of 5 from list--> {tuple.count(5)}")
print(f"min number from tuple--> {min(tuple)}")
print(f"max number from tuple--> {max(tuple)}")

print(f"sum of numbers from tuple--> {sum(tuple)}")

print(f"length of tuple--> {len(tuple)}")

##  accessing elements from tuple

for item in tuple:
    print(f"using forEach type direct value {item}")

for i in range (0,len(tuple)):
    print(f"using for index{i}----> {tuple[i]}")

print(tuple.index(5))

t=("gowtham","kumar","swamy","munu","maryada","mundamopi","chetta")

for item in t:
    if item == "gowtham":
        print(f"gowtham--> red")
    elif item == "kumar":
        print(f"kumar--> blue")
    elif item == "swamy":
        print(f"swamy--> green")
    else:
        print(f"{item }--> fol")