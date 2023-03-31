# 1. Convert Celsius to Fahrenheit and vice versa

x = float(input("Enter the Celcius: "))
y = float(input("Enter the Fahrenheit: "))

# (0°C × 9/5) + 32 = 32°F (celsius to fahrenheit)
# (32°F − 32) × 5/9 = 0°C (fahrenheit to celsius)

f = (x * 9/5 + 32)
c = (y - 32) * 5/9

print(y, "Fahrenheit to Celsius: ", format(c, '.2f'))
print(x, "Celsius to Fahrenheit", format(f, ".2f"))
