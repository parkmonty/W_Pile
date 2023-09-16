def solution(ingredient):
    hb = "1231"
    ingredient = "".join(list(map(str, ingredient)))
    count = 0

    while hb in ingredient:
        num = ingredient.index(hb)
        ingredient = ingredient[:num] + ingredient[num + 4:]
        count += 1

    return count


ingredient = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(ingredient))

ingredient = [1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(ingredient))