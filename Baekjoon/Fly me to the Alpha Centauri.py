# 문제 출처 : https://www.acmicpc.net/problem/1011
# 규칙(최소 횟수) : 1 2 3 3 4 4 5 5 5 6 6 6 7 7 7 7...
# 규칙(최소 횟수 반복) : 1 1 2 2 3 3 4 4 5 5 ...
import sys

T = int(sys.stdin.readline())

for i in range(T):
    x, y = map(int, sys.stdin.readline().split())

    # 출발점과 도착점 사이 간격
    gap = y - x
    # 1부터 1개씩 2번 2개씩 2번 ... 규칙 적용
    # 최소 횟수 반복 횟수
    n = 1
    while True:
        # 1부터 n까지 합의 2배 -> 규칙이 2번씩 반복
        total = n * (n + 1)

        if total > gap:
            # 2번씩 반복 -> total == gap 아니면 최소 횟수는 num 보다 1 or 2 만큼 크다.
            num = (n - 1) * 2
            # 최소 횟수가 num 일때 마지막 순서
            sum = (n - 1) * n
            temp = gap - sum
            # 남은 temp / n 이 1보다 크면 2번째 숫자 반대는 1번째 숫자
            if temp / n > 1:
                num += 2
            else:
                num += 1
            print(num)
            break

        elif total == gap:
            # 최소 횟수 반복 횟수 2번씩 반복 중 2번째
            print(n * 2)
            break

        n += 1


# 예제 입력 1
# 3
# 0 3
# 1 5
# 45 50
# 예제 출력 1
# 3
# 3
# 4