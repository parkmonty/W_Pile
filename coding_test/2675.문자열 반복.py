import sys

T = int(input())

for i in range(T):
    R, S = sys.stdin.readline().split()
    R = int(R)
    S = list(S)

    for j in range(len(S)):
        S[j] = S[j] * R

    print(''.join(S))