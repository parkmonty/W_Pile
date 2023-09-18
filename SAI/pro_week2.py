# 이론 문제2
# X O O O O

# 실습 문제2
import numpy as np


# 0부터 99까지의 정수를 포함하는 10 X 10 크기 행렬
test_array = np.arange(0, 100).reshape(10, 10)
print(test_array)

# 홀수로 이루어진 행렬
test_array = test_array[test_array % 2 == 1].reshape(-1, 10)
print(test_array)

# 3의 배수로 이루어진 배열
test_array = test_array[test_array % 3 == 0]
print(test_array)

# 각 요소의 제곱값
test_array = test_array ** 2
print(test_array)