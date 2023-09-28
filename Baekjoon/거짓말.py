# 문제 출처 : https://www.acmicpc.net/problem/1043
import sys


temp = sys.stdin.readline().split()
N = int(temp[0])
M = int(temp[1])

count = 0
known_p = []

know = sys.stdin.readline().split()

if int(know[0]) == 0:
    pass
else:
    count_p = int(know[0])
    
    for i in range(1, count_p + 1):
        known_p.append(int(know[i]))
        
while M > 0:
    part = sys.stdin.readline().split()
    num = int(part[0])
    
    for i in range(1, num + 1):
        if int(part[i]) not in known_p:
            M -= 1
            continue
    
    count += 1
    
sys.stdout.write(str(count))