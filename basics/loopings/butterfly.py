num=int(input("Enter a number: "))
spaces=num-1
stars=1
for i in range(1,num*2+1):
    print("* "*stars,"    "*spaces,"* "*stars)
    if i<num:
        stars+=1
        spaces-=1
    else:
        stars-=1
        spaces+=1
