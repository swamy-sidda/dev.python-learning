
def factorial(n):
    if n<0: return 0
    if n==0:return 1
    else: return n*factorial(n-1)

print(f"factorial : {factorial(5)}")
print(f"factorial : {factorial(6)}")
print(f"factorial : {factorial(7)}")