def countDigits(str):
    count=0
    for elem in str:
        if elem.isdigit():
            count+=1
    print("No of digits are ",count)

countDigits("M1a2d3a4n5a6p7a8l9l0i")

