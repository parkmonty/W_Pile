import sys

str_list = set()
N = int(sys.stdin.readline().strip())

for i in range(N):
    str_list.add(sys.stdin.readline().strip())

str_list = list(str_list)
str_list.sort()
str_list.sort(key = lambda x : len(x))

for i in str_list:
    print(i)