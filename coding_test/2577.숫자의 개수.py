import sys

count_dict = dict.fromkeys(range(10), 0)

A = list(map(int, sys.stdin.readline().split()))[0]
B = list(map(int, sys.stdin.readline().split()))[0]
C = list(map(int, sys.stdin.readline().split()))[0]

num_list = list(map(int, list(str(A * B * C))))

for i in num_list:
    count_dict[i] += 1

for i in count_dict.values():
    print(i)