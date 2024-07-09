import cv2

gray = cv2.imread("sample.png", cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(gray, 100, 200)
# cv2.imshow("Anh xam", edges)
contours = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 10)

balloon_count = 0
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 100:
        balloon_count += 1

print(f"Số lượng bóng bay: {balloon_count}")

cv2.waitKey()
cv2.destroyAllWindows()