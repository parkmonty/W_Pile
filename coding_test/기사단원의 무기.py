def solution(number, limit, power):
    sum_num = 0
    count = 0
    i = 1

    while i <= number:
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1
        if count > limit:
            sum_num += power
        else:
            sum_num += count
        i += 1
        count = 0

    return sum_num


number = 5
limit = 3
power = 2

result = solution(number, limit, power)
print(result)

number = 10
limit = 3
power = 2

result = solution(number, limit, power)
print(result)