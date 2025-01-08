import numpy as np

# numpy의 활용
# 단일 객체 저장 및 불러오기
array = np.arange(10)
np.save('saved.npy', array)

result = np.load('saved.npy')
print("result: ", result)

# 복수 객체 저장 및 불러오기
arr1 = np.arange(10)
arr2 = np.arange(10, 20)
np.savez('saveds.npz', array1=arr1, array2=arr2)

data = np.load('saveds.npz')
result1 = data['array1']
result2 = data['array2']

print("result1: ", result1, " result2: ", result2)

#======================================================================
# numpy 원소의 정렬
# 오름차순
arr3 = np.array([4, 5, 2, 9, 1])
arr3.sort()
print("arr3: ", arr3)

# 내림차순
print("arr3[::-1]: ", arr3[::-1])

# 각 열을 기준으로 정렬
arr4 = np.array([[5, 9, 10, 3, 1], [8, 3, 4, 2, 5]])
print(arr4)

arr4.sort(axis=0)
print(arr4)


#================================================================
# 균일한 간격으로 데이터 생성
arr5 = np.linspace(0, 10, 5)
print(arr5)


#================================================================
# 난수의 재연 (실행마다 결과 동일)
np.random.seed(3) # 각 시드마다 동일한 결과
print(np.random.randint(0, 10, (2, 3)))


#================================================================
# numpy 배열 객체 복사
arr6 = np.arange(10)
arr7 = arr6 # 동일한 주소를 가리키게 됨
arr7[0] = 99

print(arr6)

arr8 = arr6.copy()
arr8[0] = 9999

print("arr6: ", arr6, " arr8: ", arr8)


#================================================================
# 중복된 원소 제거
arr9 = np.array([1, 1, 2, 2, 2, 3, 3, 4])
print(np.unique(arr9))

