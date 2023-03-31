# 4. WAP that prompts user to enter number the process will continue until user enters - 1.
# Finally the program print the count of prime & composite number.


while True:
    c = 0
    p = 0
    n = int(input("Enter a number: "))
    if (n == -1):
        break
    else:
        def prime(n):
            for i in range(2, n):
                if n % i == 0:
                    break
            else:
                p = p + 1
            return p

        def composite(n):
            x = 0
            for i in range(2, n):
                if (n % i) == 0:
                    x = i
                if x > 1:
                    c = c + 1
                    return c
                c = composite(n)
                p = prime(n)

print("Number of Composite: ", c)
print("Number of Prime: ", p)
