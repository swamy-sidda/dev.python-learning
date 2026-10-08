num = int(input("Enter a number: "))
spaces = num
stars = 1
for i in range(1,num*2+1):
    print("  "*spaces,"* "*stars," "*int(spaces//2),"* "*stars)
    if(i<num):
        spaces = spaces+1
        stars = stars+2
    else:
        spaces = spaces-1
        stars = stars-2