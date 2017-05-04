a = int(input())
b = int(input())
print((((a + b) // b - 1) * a + ((a + b) // a - 1) * b) // (a // b + b // a))
