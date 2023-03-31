# 3. Find the distance between 2 points.

x = float(input("Enter the point of x: "))
y = float(input("Enter the point of y: "))

if (x > y):
    d = x - y
else:
    d = y - x

print("The distance between 2 points: ", d)
