N = int(input())
num = 0
cnt = 1
i = 1

while cnt < N:
    num = 6 * i
    cnt += num
    i += 1

print(i)