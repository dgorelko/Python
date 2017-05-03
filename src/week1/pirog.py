# a - rubles
a = int(input())
# b - kopek
b = int(input())
# n - number of pirog
n = int(input())
# cost in kopeks
cost = (a * 100 + b)*n
print(cost // 100, cost % 100)
