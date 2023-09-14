def div_count(number):
    count = 0

    for i in range(1, number + 1):
        if number % i == 0:
            count += 1

    return count

def solution(number, limit, power):
    num_list = []

    for i in range(1, number + 1):
        num_list.append(div_count(i))

    for j in range(len(num_list)):
        if num_list[j] > limit:
            num_list[j] = power

    return sum(num_list)


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