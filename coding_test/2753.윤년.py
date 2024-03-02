num = int(input())

if num % 400 == 0:
    print(1)
elif num % 100 != 0 and num % 4 == 0:
    print(1)
else:
    print(0)