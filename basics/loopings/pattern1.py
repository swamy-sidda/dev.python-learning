row = int(input("Enter the number of rows: "))
for i in range(1,row+1):
    print("  "*int(row-i+1),end="")
    for n in range(1,i+1):
        print(n,end=" ")
    print()