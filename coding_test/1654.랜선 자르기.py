# Binary Search (이진탐색)
import sys

K, N = map(int, sys.stdin.readline().split())
wire_len = [int(sys.stdin.readline().strip()) for _ in range(K)]
start, end = 1, max(wire_len)

while start <= end:
    mid = (start + end) // 2
    count = 0

    for i in wire_len:
        count += (i // mid)

    if count >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)