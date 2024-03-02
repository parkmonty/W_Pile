import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    H, W, N = map(int, sys.stdin.readline().split())

    if N % H != 0:
        print((N % H) * 100 + (N // H + 1))
    else:
        print(H * 100 + (N // H))