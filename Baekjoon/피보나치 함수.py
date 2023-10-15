# 문제 출처 : https://www.acmicpc.net/problem/1003
import sys

def count(N):
    print(str(count_0(N)) + " " + str(count_1(N)))

def count_0(N):
    if N == 0:
        return 1
    elif N == 1:
        return 0
    else:
        return count_0(N - 1) + count_0(N - 2)

def count_1(N):
    if N == 1:
        return 1
    elif N == 0:
        return 0
    else:
        return count_1(N - 1) + count_1(N - 2)
    
    
T = []
T.append(sys.stdin.readline())

for i in T:
    count(int(i))