i=1;
for j in range(1,10):
    for k in range(1,10):
        if(j%2==1):
            print(i,end=" ")
            i=i+1
        else:
            i=i-1
            print(i,end=" ")
    print()