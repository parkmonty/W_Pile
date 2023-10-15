# 문제 출처 : https://www.acmicpc.net/problem/1003
import sys

def count(N):
    num_list = [0, 0]
    if N == 1:
        num_list[1] += 1
        return num_list
    elif N == 0:
        num_list[0] += 1
        return num_list
    else:
        num_list[0] = count(N - 1)[0] + count(N - 2)[0]
        num_list[1] = count(N - 1)[1] + count(N - 2)[1]
        return num_list
    
T = []
T.append(sys.stdin.readline())

for i in T:
    c = count(int(i))
    print(str(c)[0] + " " + str(c)[1])