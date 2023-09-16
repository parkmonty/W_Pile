def solution(food):
    result_food = ""

    for i in range(1, len(food)):
        result_food += str(i) * (food[i] // 2)
    result_food = result_food + "0" + result_food[::-1]

    return result_food


food = [1, 3, 4, 6]
print(solution(food))

food = [1, 7, 1, 2]
print(solution(food))