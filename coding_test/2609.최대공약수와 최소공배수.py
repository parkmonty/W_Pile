def gcd(N, M):
    x, y = N, M
    while True:
        x, y = y, x % y
        if y == 0:
            return x


import sys

N, M = map(int, sys.stdin.readline().split())
num = gcd(N, M)

print(num)
print(int((N*M) / num))