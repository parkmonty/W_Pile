import sys

n = int(sys.stdin.readline().strip())
check_stack = list(range(1, n + 1))
stack = []
result = []

for _ in range(n):
    num = int(sys.stdin.readline().strip())

    while True:
        if len(stack) == 0:
            temp = check_stack.pop(0)
            stack.append(temp)
            result.append('+')
        else:
            temp = stack[-1]
            if temp == num:
                result.append('-')
                stack.pop()
                break
            else:
                if temp > num:
                    result = 'NO'
                    break
                stack.append(check_stack.pop(0))
                result.append('+')

    if result == 'NO':
        break

if result == "NO":
    print("NO")
else:
    for i in result:
        print(i)

#############################################################

cnt = 1
temp = 0
stack = []
result = []

N = int(sys.stdin.readline().strip())
for i in range(N):
    num = int(sys.stdin.readline().strip())
    while cnt <= num:
        stack.append(cnt)
        result.append('+')
        cnt += 1

    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        temp = 1
        break

if temp:
    print("NO")
else:
    for i in result:
        print(i)