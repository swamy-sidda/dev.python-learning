num = int(input("Enter a number: "))
spaces = num;
for i in range(1,num+1):
    print("  "*spaces,"*   "*i)
    spaces = spaces-1