# 오답
import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
check_num = list(map(int, sys.stdin.readline().split()))

A.sort()

for i in check_num:
    left = 0
    right = N - 1

    while left < right:
        mid = (left + right)//2

        if A[mid] > i:
            right = mid - 1
        elif A[mid] < i:
            left = mid + 1
        else:
            print(1)
            break

    if left == right:
        if A[left] != i:
            print(0)
        else:
            print(1)

########################################################
# 정답

N = int(input())
nArray = set(map(int, input().split()))
M = int(input())
mArray = list(map(int, input().split()))

for i in range(M):
    if mArray[i] in nArray:
        print("1")
    else:
        print("0")