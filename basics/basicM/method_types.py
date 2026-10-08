def func():
    print("No arguments method")
    return  "Method execution is completed"
func()
print(func())

def addInteger(a,b):
    # print(a+b)
    return f"Method execution is completed {a+b}"
print(addInteger(1,2))


def addMultiple(a,*b):
    sum=a;
    for item in b:
        sum+=item
    return f"Sum of variable arguments is  {sum}"

print(addMultiple(1,2,3,4))

def addMultiple(a,**b):
    sum=a;
    for key,value in b.items():
        sum+=value
        print(f"key : {key} , value : {value}")
    return f"Sum of variable arguments is  {sum}"

print(addMultiple(1,d=1,b=2,c=3,e=4))