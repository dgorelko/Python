m = int(input())
n = int(input())
o = 1 // (1 + n)
f = 1 // (1 + (m * (1 - o)) % (n + 2 * o))
d = {0: 'NO', 1: 'YES'}
print(d[f])
