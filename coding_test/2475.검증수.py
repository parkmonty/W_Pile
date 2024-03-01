import sys

sum = 0
num_list = list(map(int, sys.stdin.readline().split()))

for i in num_list:
    sum += i ** 2

print(sum % 10)