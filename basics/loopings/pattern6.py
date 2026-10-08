num=5
spaces=num;
stars=1;
for i in range(1,num*2+1):
    print("  "*spaces,"* "*stars)
    if(i<num):
        spaces=spaces-1
        stars=stars+1
    else:
        spaces=spaces+1
        stars=stars-1