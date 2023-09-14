def div_count(number):
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    return count

def solution(number, limit, power):
    sum_num = 0

    for i in range(1, number + 1):
        if div_count(i) > limit:
            sum_num += power
        else:
            sum_num += div_count(i)

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