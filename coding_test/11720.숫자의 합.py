import sys

N = int(sys.stdin.readline().strip())
num = sys.stdin.readline().strip()
sum = 0

for i in range(N):
    sum += int(num[i])

print(sum)