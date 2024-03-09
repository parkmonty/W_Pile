import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
num_list = []
sum = 0

for i in range(N):
    num = int(sys.stdin.readline().strip())
    num_list.append(num)
    sum += num

num_list.sort()
cnt = Counter(num_list).most_common()

print(round(sum/N))
print(num_list[len(num_list)//2])
if N == 1:
    print(num_list[0])
elif cnt[0][1] != cnt[1][1]:
    print(cnt[0][0])
else:
    print(cnt[1][0])
print(num_list[-1] - num_list[0])