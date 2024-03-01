import sys

a = list()

for i in range(9):
    a += list(map(int, sys.stdin.readline().split()))

num_max = max(a)
index = a.index(num_max) + 1

print(num_max)
print(index)