import sys
from string import ascii_lowercase

S = list(sys.stdin.readline().strip())
count_dict = dict.fromkeys(list(ascii_lowercase), -1)

for i in range(len(S)):
    if count_dict[S[i]] == -1:
        count_dict[S[i]] = i

for i in count_dict.values():
    sys.stdout.write(str(i) + ' ')