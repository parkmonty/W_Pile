# 문제 출처 : https://www.acmicpc.net/problem/1013
# 전파 패턴 : (100+1+ | 01)+
import sys


T = int(sys.stdin.readline())
temp = 0

while temp < T:
    temp += 1
    s_num = sys.stdin.readline()
    
    index = 0
    while index < len(s_num):
        pre_index = index.copy()
        
        if index + 2 < len(s_num):
            if s_num[index : index + 3] == "100":
                index_1 = s_num[index + 3:].find("1")
                index_0 = s_num[index_1:].find("0")
                
                if index_1 == -1:
                    print("NO")
                    break
                elif index_0 == -1:
                    print("YES")
                    break
                else:
                    if index_0 - index_1 == 1:
                        index = index_0
                    else:
                        if len(s_num) > index_0 + 1:
                            if s_num[index_0 + 1] == "1":
                                index = index_0
                            else:
                                index = index_0 - 1
        
        if index + 1 < len(s_num):
            if s_num[index : index + 2] == "01" and index + 2 == len(s_num):
                print("YES")
                break
            elif s_num[index : index + 2] == "01" and index + 2 < len(s_num):
                index += 2
                
        if pre_index == index:
            print("NO")
            break
        
        if index + 1 == len(s_num):
            print("YES")