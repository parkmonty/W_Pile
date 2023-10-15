# 문제 출처 : https://www.acmicpc.net/problem/1003
import sys

def count(N):
    zero = [1, 0]
    one = [0, 1]
    
    if N >= 2:
        for i in range(2, N + 1):
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
            
    sys.stdout.write(f"{zero[N]} {one[N]}\n")
    

T = int(sys.stdin.readline())

for _ in range(T):
    count(int(sys.stdin.readline()))