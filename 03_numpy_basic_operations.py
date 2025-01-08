import numpy as np

array = np.random.randint(1, 10, 4).reshape(2, 2)
result_array = array * 10
print("array: ", array, " result_array: ", result_array)

#==============================================================
# 서로 다른 형태의 numpy 연산
# numpy는 서로 다른 형태의 배열을 연산할 때는 행 우선으로 수행됨
# 브로드캐스트: 형태가 다른 배열을 연산할 수 있도록 배열의 형태를 동적으로 변환
# [[0 1]] -> [[0 1]  +  [[0 1]  =  [[0 2]
#             [0 1]]     [2 3]]     [2 4]]
arr1 = np.arange(4).reshape(2, 2)
arr2 = np.arange(2)
arr3 = arr1 + arr2

print("arr3: ", arr3)

arr4 = np.arange(0, 8).reshape(2, 4)
arr5 = np.arange(0, 8).reshape(2, 4)
arr6 = np.concatenate([arr4, arr5], axis=0)
print("arr6: ", arr6)

arr7 = np.arange(4).reshape(4, 1)
arr8 = arr6 + arr7
print("arr8: ", arr8)

#=================================================================
# numpy의 마스킹 연산
# 마스킹: 각 원소에 대해 체크한다. ex) 각 원소에 대해 5보다 작다면 True, 크면 False
arr9 = np.arange(16).reshape(4, 4)
print("arr9: ", arr9)

arr10 = arr9 < 10
print("arr10: ", arr10)

arr9[arr10] = 100
print("arr9: ", arr9)

#===============================================================
# numpy의 집계 함수
arr11 = np.arange(16).reshape(4, 4)

print("최대값: ", np.max(arr11))
print("최소값: ", np.min(arr11))
print("합 계: ", np.sum(arr11))
print("평균값: ", np.mean(arr11))
print("각 행에 대한 합계: ", np.sum(arr11, axis=0))
print("각 열에 대한 합계: ", np.sum(arr11, axis=1))
