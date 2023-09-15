def solution(k, m, score):
    score.sort()
    last_num = len(score)
    rest_num = last_num % m

    index = rest_num
    total = 0

    while index < last_num:
        total += score[index]
        index += m

    return total * m


k = 3
m = 4
score = [1, 2, 3, 1, 2, 3, 1]

print(solution(k, m, score))

k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

print(solution(k, m, score))