import sys

product_count, weight_max = map(int, sys.stdin.readline().split())
sum_value = [[0 for _ in range(weight_max + 1)] for _ in range(product_count + 1)]

value = [[0, 0]]
for _ in range(product_count):
    value.append(list(map(int, sys.stdin.readline().split())))

for i in range(1, product_count + 1):
    for j in range(1, weight_max + 1):
        w, val = value[i]
        if j >= w:
            sum_value[i][j] = max(sum_value[i - 1][j], sum_value[i - 1][j - w] + val)
        else:
            sum_value[i][j] = sum_value[i - 1][j]

print(sum_value[product_count][weight_max])