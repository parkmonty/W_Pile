import sys

case_num = int(sys.stdin.readline().strip())

for i in range(case_num):
    score = 1
    score_sum = 0
    ox_list = list(sys.stdin.readline().strip())

    for j in range(len(ox_list)):
        if ox_list[j] == 'O':
            score_sum += score
            score += 1
        else:
            score = 1

    print(score_sum)