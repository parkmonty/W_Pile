# 중복되는 숫자 불가능
import sys

# T_case : 테스트 케이스 개수
T_case = int(sys.stdin.readline().strip())

for i in range(T_case):
    # N : 자료 개수, M : 원하는 자료 현재 위치
    N, M = map(int, sys.stdin.readline().split())
    # R : 자료의 중요도 및 순서
    R = list(map(int, sys.stdin.readline().split()))
    # cnt : 출력되는 순서
    cnt = 0

    if N == 1:
        cnt += 1
        print(cnt)
        continue

    ck_num = R[M]

    while True:
        # MI : 현재 자료 중 가장 높은 중요도의 인덱스
        MI = R.index(max(R))
        cnt += 1

        if R[MI] == ck_num:
            print(cnt)
            break
        else:
            R = R[MI + 1:] + R[:MI]

####################################################
import sys
from collections import deque

T_case = int(sys.stdin.readline().strip())

for _ in range(T_case):
    # N : 자료 개수, M : 원하는 자료 현재 위치
    N, M = map(int, sys.stdin.readline().split())
    # R : 자료의 중요도 및 순서
    R = deque(map(int, sys.stdin.readline().split()))
    R = deque((i, idx) for idx, i in enumerate(R))
    # cnt : 출력되는 순서
    cnt = 0

    while True:
        if R[0][0] == max(R, key=lambda x : x[0])[0]:
            cnt += 1
            if R[0][1] == M:
                print(cnt)
                break
            else:
                R.popleft()
        else:
            R.append(R.popleft())