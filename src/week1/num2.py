N = int(input())
hundred = N // 100
dozen = N % 100 // 10
units = N % 100 % 10
print(hundred + dozen + units)
