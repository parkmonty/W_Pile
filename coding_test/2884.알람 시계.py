import sys

H, M = map(int, sys.stdin.readline().split())

if M < 45:
    M = M - 45 + 60

    if H == 0:
        H = 23
    else:
        H = H - 1

else:
    M = M - 45

print(H, M)