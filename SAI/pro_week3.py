# 이론 문제
# X O X X O X


# 실습 문제
import numpy as np


arr = np.array([['이지헌', 20011266, 2.1],
                ['이승하', 22012312, 3.5],
                ['노주호', 22012414, 4.1],
                ['사예진', 21032121, 3.1],
                ['이준영', 20032132, 3.8],
                ['이주호', 19321327, 1.9],
                ['노지헌', 21052136, 2.7],
                ['이예진', 18032132, 3.8],
                ['노승하', 23164723, 0.8],
                ['서준영', 19327213, 4.5]])

index = []
temp = []
count = 0

# F학점인 학생 인덱스를 index 리스트에 저장
for i in range(len(arr)):
    if float(arr[i, 2]) < 2.0:
        index.append(i)

# delete로 index가 감소 하는 것을 보정하기 위한 변수 count
for i in index:
    arr = np.delete(arr, i - count, axis = 0)
    count += 1

# 정렬 전 인덱스를 리스트 arr_ord에 저장
arr_ord = np.argsort(arr[::, 2])[::-1]

for i in arr_ord:
    temp.append(arr[i, ::])
arr = np.array(temp)

print(arr)

# 해당 학점에 해당하는 학생의 인덱스 리스트 저장
index_A = []
index_B = []
index_C = []

for i in range(len(arr)):
    if float(arr[i, 2]) >= 4.0:
        index_A.append(i)
    elif float(arr[i, 2]) >= 3.0:
        index_B.append(i)
    else:
        index_C.append(i)
        
print(arr[index_A[0]:index_A[-1] + 1])
print(arr[index_B[0]:index_B[-1] + 1])
print(arr[index_C[0]:index_C[-1] + 1])