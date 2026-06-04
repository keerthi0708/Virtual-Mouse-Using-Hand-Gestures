import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    if not success:
        print("Camera not detected")
        break

    cv2.imshow("Camera Test", img)

    if cv2.waitKey(1) == 27:  # ESC
        break

cap.release()
cv2.destroyAllWindows()