# 4. Convert the given time into hour/minute/seconds.
# (The input is taken as second = 8523 - hh: mm: ss)
# int S = seconds % 60
# int H = seconds / 60
# int M = H % 60
# H = H / 60


s = int(input("Enter the Time in Seconds: "))

sec = s % 60
h = s / 60
m = h % 60
h = h / 60

print(int(h), ":", int(m), ":", int(sec))
