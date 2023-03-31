# 2. Area of a triangle using Hirons formula.
# S = A + B + C / 2
# Area = root/s*(s-a)*(s-b)*(s-c)
# root = **0.5

a = float(input("Enter the Side A of the Triangle: "))
b = float(input("Enter the Side B of the Triangle: "))
c = float(input("Enter the Side C of the Triangle: "))

s = (a + b + c) / 2
area = s*(s-a)*(s-b)*(s-c)
area = area ** 0.5  # Formula of square root is n ** 0.5

print("Area of the triangle: %0.3f" % area)
