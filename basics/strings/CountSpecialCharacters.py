def countSpecialCharacters(string):
    count = 0
    for ele in string:
        if not ele.isdigit() and not ele.isalpha():
            count += 1
    print("number of special characters is ", count)


countSpecialCharacters("K@u#m$a%r^a S)w(a{m}i/?")
