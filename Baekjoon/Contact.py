# 문제 출처 : https://www.acmicpc.net/problem/1013
# 전파 패턴 : (100+1+ | 01)+

import sys
# 정규 표현식 : 특정한 규칙을 가진 문자열 패턴을 사용하는 방식
# github 정리 : https://github.com/parkmonty/W_Pile/blob/main/SAI/%EC%A0%95%EA%B7%9C%ED%91%9C%ED%98%84%EC%8B%9D(re).ipynb
import re


T = int(sys.stdin.readline())
result = []

# re.compile("패턴")
for _ in range(T):
    num_s = sys.stdin.readline().strip()
    pattern = re.compile("(100+1+|01)+")
    match_result = pattern.fullmatch(num_s)
    
    if match_result:
        result.append("YES")
    else:
        result.append("NO")
        
for i in result:
    # 속도 향상을 위해 print 대신 sys.stdout.write 사용
    # print -> 메모리 적음 / 속도 느림 / 줄바꿈하여 출력
    # sys.stdout.write() -> 메모리 큼 / 속도 빠름 / 줄바꿈없이 바로이어서 출력
    sys.stdout.write(i + "\n")