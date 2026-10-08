num=int(input("enter number:"))
i=1;
for j in range(1,num+1):
    print("  "*int(num-j),f"{num-j+1}"" "*int(j),end="\n",)