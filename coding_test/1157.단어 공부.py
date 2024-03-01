import sys

check = list(sys.stdin.readline().strip().upper())
count = dict.fromkeys(check, 0)

for i in check:
    if i in count:
        count[i] += 1

num_max = max(count.values())
name = list()

for j in count.items():
    if num_max == j[1]:
        name.append(j[0])

print('?') if len(name) != 1 else print(name[0])