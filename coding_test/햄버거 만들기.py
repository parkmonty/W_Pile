def solution(ingredient):
    count = 0
    index = 0

    while index < len(ingredient) - 3:
        if ingredient[index : index + 4] == [1, 2, 3, 1]:
            count += 1
            del ingredient[index : index + 4]
            index = -1
        index += 1

    return count


ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))

ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(ingredient))