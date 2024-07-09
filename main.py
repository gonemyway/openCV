import  cv2

# Khoi tao bo phan loai khuon mat
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Khoi tao bien dem so khuon mat
face_count = 0

cap = cv2.VideoCapture(0)
key = cv2.waitKey(1)

while True:
    ret, frame = cap.read()
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # Phat hien khuon mat
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
        # Ve khung chu nhat bao quanh khuon mat
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
            # Neu nhan dien duoc khuon mat thi luu lai
            if cv2.waitKey(1) & key == ord('s'):
                face_count += 1
                cv2.imwrite(f'{face_count}.png', gray[y:y+h, x:x+w])
        cv2.imshow("A", frame)

        if cv2.waitKey(1) & key == ord('q'):
            break


cap.release()
cv2.destroyAllWindows()