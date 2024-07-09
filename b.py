import cv2
import numpy as np


def detect_circles(image_path):
    # Đọc hình ảnh
    img = cv2.imread(image_path, cv2.IMREAD_COLOR)
    output = img.copy()

    # Chuyển sang ảnh xám
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Làm mịn ảnh để giảm nhiễu
    gray = cv2.medianBlur(gray, 5)

    # Phát hiện các hình tròn bằng Hough Circles
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100, param1=50, param2=30, minRadius=20, maxRadius=400)

    # Vẽ các hình tròn tìm được
    if circles is not None:
        circles = np.round(circles[0, :]).astype("int")
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 4)  # Vẽ vòng tròn màu xanh lá cây
            cv2.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)  # Vẽ tâm vòng tròn

    # Hiển thị ảnh kết quả
    cv2.imshow("detected circles", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Trả về số lượng vòng tròn được phát hiện
    return len(circles) if circles is not None else 0


# Đường dẫn đến tập tin hình ảnh
image_path = 'sample.png'
num_circles = detect_circles(image_path)
print(f"Số lượng quả bóng tìm thấy: {num_circles}")
