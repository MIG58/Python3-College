r1 = int(input("Enter the start range: "))
r2 = int(input("Enter the end range: "))

for i in range(r1, r2+1):
    c = 0
    for j in range(2, i):
        if (i % j) == 0:
            c = 1
            break
    if (c == 0):
        print(i, end=' ')
