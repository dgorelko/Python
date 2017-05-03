n = int(input())
a = n % 100
b = n // 100
b = b // 10 + b % 10 * 10
print(a-b+1)
