# 2. WAP to find the maximum of 3 numbers.
a = int(input("Enter the value of A: "))
b = int(input("Enter the value of B: "))
c = int(input("Enter the value of C: "))

if a > b:
    if a > c:
        print("A is the maximum")
    else:
        print("C is the maximum")
else:
    if b > c:
        print("B is the maximum")
    else:
        print("C is the maximum")
