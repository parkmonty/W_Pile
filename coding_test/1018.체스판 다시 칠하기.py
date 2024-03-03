import sys

n, m = map(int, sys.stdin.readline().split())
board = []
result = []

for _ in range(n):
    # board.append(input())
    board.append(sys.stdin.readline().strip())

for i in range(n - 7):
    for j in range(m - 7):
        draw1 = 0
        draw2 = 0

        for k in range(i, i + 8):
            for h in range(j, j + 8):
                if (k + h) % 2 == 0:
                    if board[k][h] != 'B':
                        draw1 += 1
                    if board[k][h] != 'W':
                        draw2 += 1
                else:
                    if board[k][h] != 'W':
                        draw1 += 1
                    if board[k][h] != 'B':
                        draw2 += 1

        result.append(draw1)
        result.append(draw2)

print(min(result))