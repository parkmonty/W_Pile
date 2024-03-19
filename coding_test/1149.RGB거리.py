import sys

house_count = int(sys.stdin.readline().strip())
RGB_price = [list(map(int, sys.stdin.readline().split())) for _ in range(house_count)]

min_price = [[0, 0, 0] for _ in range(house_count)]
min_price[0] = RGB_price[0]

for i in range(1, house_count):
    min_price[i][0] = min(min_price[i - 1][1], min_price[i - 1][2]) + RGB_price[i][0]
    min_price[i][1] = min(min_price[i - 1][0], min_price[i - 1][2]) + RGB_price[i][1]
    min_price[i][2] = min(min_price[i - 1][0], min_price[i - 1][1]) + RGB_price[i][2]

min_price = min(min_price[-1])
print(min_price)