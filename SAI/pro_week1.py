# 이론 문제1
# O X O X O

# 실습 문제1
n = int(input())
m = int(input())

i = 0
num = list(range(n, m + 1))

while len(num) > i:
  for j in range(2, num[i] // 2 + 1):
    if num[i] % j == 0:
      del num[i]
      i -= 1
      break
  i += 1

for n in num:
  print(n)
print(i)