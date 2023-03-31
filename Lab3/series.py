# 3.to sum the series: 1/2² + 2/3³ + 3/4⁴

n = int(input("Enter the range: "))

ser = 0
for i in range(1, n+1):
    ser += i / ((i+1)**(i+1))

print(ser)
