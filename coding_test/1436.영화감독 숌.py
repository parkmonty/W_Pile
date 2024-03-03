# Brute Force 방법 사용
import sys

N = int(sys.stdin.readline().strip())

dead_num = 666
count = 0

while True:
    if '666' in str(dead_num):
        count += 1

    if count == N:
        break

    dead_num += 1

print(dead_num)