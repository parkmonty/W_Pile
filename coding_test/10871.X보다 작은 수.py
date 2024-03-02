import sys

N, X = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

for i in list(filter(lambda x : x < X, num_list)):
    print(i)