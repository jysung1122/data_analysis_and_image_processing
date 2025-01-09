import cv2

image = cv2.imread('image/image_basic.png')
# 픽셀 수 및 이미지 크기 확인
print(image.shape)
print(image.size)

# 이미지 numpy 객체의 특정 픽셀을 가리키기
px = image[100, 100]

# BGR 순서로 출력된다.
print(px)

# r 값만 출력하기
print(px[2])


#===============================================================
# 특정 범위 픽셀 변경
image[0:100, 0:100] = [0, 0, 0]
cv2.imshow('hi', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#===============================================================
# ROI 추출 및 복사
roi = image[0:100, 100:200]
image[0:100, 0:100] = roi
cv2.imshow('hi', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#===============================================================
# 픽셀 별 색상 다루기
image[:, :, 2] = 0
cv2.imshow('hi', image)
cv2.waitKey(0)
cv2.destroyAllWindows()



