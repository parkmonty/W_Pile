def digit_sum(N):
    sum = 0
    while N > 0:
        sum += N%10
        N //= 10
    return sum


N = int(input())
cnt = 0
result = 0

while N > 0:
    N -= 1
    cnt += 1

    if digit_sum(N) == cnt:
        result = N

print(result)

#####################################

for i in range(1, N+1):
    result = digit_sum(i) + i
    if N == result:
        print(i)
        break
    if i == N:
        print(0)