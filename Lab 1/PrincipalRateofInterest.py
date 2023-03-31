# 5. Calculate the total amount with given principle and rate of interest.

p = float(input("Enter the principle amount: "))
r = float(input("Enter the rate of interest: "))

total_amount = p + (p * r / 100)

print("The total amount is:", total_amount)
