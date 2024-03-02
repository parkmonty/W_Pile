import sys

remain_set = set()

for i in range(10):
    num = int(sys.stdin.readline().strip())
    remain_set.add(num % 42)

print(len(remain_set))