import sys

def prime_num(num):
    ck = 1

    if num == 1:
        ck = 0

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            ck = 0
            break

    if ck:
        print(num)


N, M = map(int, sys.stdin.readline().split())

for i in range(N, M+1):
    prime_num(i)