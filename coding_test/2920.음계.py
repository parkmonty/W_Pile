import sys

num_list = list(map(int, sys.stdin.readline().split()))
num = [1, 2, 3, 4, 5, 6, 7, 8]

if num_list == num:
    print('ascending')
elif num_list == sorted(num, reverse=True):
    print('descending')
else:
    print('mixed')