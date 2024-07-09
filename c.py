import cv2
import imutils
# import  numpy as np

img = cv2.imread('sample1.png', cv2.IMREAD_GRAYSCALE)
# img = cv2.resize(img, dsize=None, fx=0.5, fy=0.5)
threshold = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 15, 8)
# cv2.imshow('Anh nhi phan', threshold)
# cv2.waitKey()
contours = cv2.findContours(threshold, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours, key=cv2.contourArea, reverse=False)

number = 0

for c in contours:
    (x, y, w, h) = cv2.boundingRect(c)
    if (40 < w < 90) and (80 < h < 180):
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)
        number += 1
        crop = img[y:y+h, x:x+w]
        cv2.imwrite(f'{number}.png', crop)

cv2.imshow('Pic', img)
cv2.waitKey()
cv2.destroyAllWindows()