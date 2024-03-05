import sys
from math import sqrt

cnt = 0
N = int(sys.stdin.readline().strip())
num_list = list(map(int, sys.stdin.readline().split()))

for i in num_list:
    if i == 1:
        cnt += 1
        continue

    for j in range(2, int(sqrt(i)) + 1):
        if i % j == 0:
            cnt += 1
            break

print(N - cnt)