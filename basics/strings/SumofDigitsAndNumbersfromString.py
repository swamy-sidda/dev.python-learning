def digitSum(str):
    sum = 0
    for ele in str:
        if ele.isdigit():
            sum += int(ele)
    print("Sum of digits is ", sum)


digitSum("M1a2d3a4n5a6p7a8l9l0i")


def numberSum(string):
    sum = 0
    str = ''
    for ele in string:
        if ele.isdigit():
            str = str + ele
        else:
            if str:
                sum += int(str)
            str = ''
    if str:
        sum += int(str)
    print("Sum of numbers is ", sum)


numberSum("12M11a2d3a4n5a6p7a8l9l20i0-1")
