def enterString(str):
    str = str.lower()
    count = 0
    for elem in str:
        if elem == 'a' or elem == 'e' or elem == 'i' or elem == 'o' or elem == 'u':
            count += 1
    print("Number of vowels in String ", count)
    count = 0
    for elem in str:
        if elem.isalpha() and elem != 'a' and elem != 'e' and elem != 'i' and elem != 'u':
            count += 1
    print("Number of consonents  in String ", count)


enterString("Madanapalli vikatakavi")


def countTypes(str):
    vowel = 0
    consonant = 0
    for elem in str:
        if elem in 'aeiouAEIOU':
            vowel += 1
        if elem.isalpha() and elem not in 'aeiouAEIOU':
            consonant += 1
    print("Number of vowels in String ", vowel)
    print("Number of consonents in String ", consonant)


countTypes("Madanapalli vikatakavi")
