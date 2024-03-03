import sys

while True:
    N = int(sys.stdin.readline().strip())

    if N == 0:
        break
    elif str(N) == str(N)[::-1]:
        print('yes')
    else:
        print('no')