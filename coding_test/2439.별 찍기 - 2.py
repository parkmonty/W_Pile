count = int(input())

for i in range(count):
    print(' ' * (count - (i + 1)) + '*' * (i + 1))