# 3. WAP to swap 2 variables without using 3rd variable.

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Before swapping: a =", a, ", b =", b)

a = a + b
b = a - b
a = a - b

print("After swapping: a =", a, ", b =", b)
