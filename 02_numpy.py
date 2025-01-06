import numpy as np

list_data = [1, 2, 3]
array = np.array(list_data) # 특정한 리스트 데이터를 numpy 자료형으로 바꿔줌

print("array: ", array)
print("array.size: ", array.size)
print("array.dtype: ", array.dtype)
print("array[2]: ", array[2])

#=======================================================
# 0부터 3까지의 배열 만들기
array1 = np.array(4)
print("array1: ", array1)

array2 = np.zeros((4, 4), dtype=float)
print("array2: ", array2)

array3 = np.ones((3, 3), dtype=str)
print("array3: ", array3)

#======================================================
# 0부터 9까지 랜덤하게 초기화 된 배열 만들기
array4 = np.random.randint(0, 10, (3, 3))
print("array4: ", array4)

#======================================================
# 평균이 0이고, 표준 편차가 1인 표준 정규를 띄는 배열
array5 = np.random.normal(0, 1, (3, 3))
print("array5: ", array5)

#=====================================================
# 배열 가로로 합치기
array6 = np.array([1, 2, 3])
array7 = np.array([4, 5, 6])
array8 = np.concatenate([array6, array7])
print("array8.shape: ", array8.shape)
print("array8: ", array8)

#====================================================
# 배열 형태 바꾸기
array9 = np.array([1, 2, 3, 4])
array10 = array9.reshape((2,2))
print("array10: ", array10)

#===================================================
# 배열 세로로 합치기
array11 = np.arange(4).reshape(1, 4)  # 0, 1, 2, 3을 1차원 배열로 만들기
array12 = np.arange(8).reshape(2, 4)  # 0 ~ 7을 2차원 배열로 만들기

print("array11: ", array11)
print("array12: ", array12)

array13 = np.concatenate([array12, array11], axis=0)
print("array13: ", array13)

#===================================================
# 배열 나누기
array14 = np.arange(8).reshape(2, 4)
# 두 번째 인자: 배열을 나눌 인덱스 위치 (리스트 형태), 세 번째 인자: 배열을 나눌 축 (axis=0: 행, axis=1: 열)
left, right = np.split(array14, [2], axis=1)
print("left: ", left, " right: ", right)
print("left.shape: ", left.shape, " right.shape: ", right.shape)