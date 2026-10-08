amount = float(input("Enter your amount: "))
if amount >= 500:
    print("500 notes are ", amount//500)
    amount %= 500
if amount >=200:
    print("200 notes are ", amount//200)
    amount %= 200
if amount >=100:
    print("100 notes are ", amount//100)
    amount %= 100
if amount >=50:
    print("50 notes are ", amount//50)
    amount %= 50
if amount >=20:
    print("20 notes are ", amount//20)
    amount %= 20
if amount >=10:
    print("10 notes are ", amount//10)
    amount %= 10
    print(f"amount balance is {amount:.2f}")