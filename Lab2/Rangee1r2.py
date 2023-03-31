# 6. Calculate the sumation of the number of the given range r1 and r2

r1 = int(input("Enter the 1st range: "))
r2 = int(input("Enter the 2nd range: "))

sum = 0

for i in range(r1, r2):
    sum += i

print("Sumation of the given range: ", sum)
