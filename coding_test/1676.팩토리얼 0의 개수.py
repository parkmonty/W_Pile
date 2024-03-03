N = int(input())
multi = 1

for i in range(N):
    multi = multi * (i + 1)

multi = str(multi)[::-1]
count = 0

for i in multi:
    if i == '0':
        count += 1
    else:
        print(count)
        break