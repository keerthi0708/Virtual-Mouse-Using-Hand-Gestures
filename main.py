import cv2
import numpy as np
import pyautogui
import time
import HandTrackingModule as htm

cap = cv2.VideoCapture(0)

detector = htm.handDetector()

screenW, screenH = pyautogui.size()
plocX, plocY = 0, 0
clocX, clocY = 0, 0
smoothening = 7

lastClick = 0

while True:

    success, img = cap.read()
    img = cv2.flip(img, 1)

    img = detector.findHands(img)

    lmList = detector.findPosition(img)

    if len(lmList) != 0:

        x1, y1 = lmList[8][1:]

        hCam, wCam, _ = img.shape

        screenX = np.interp(x1, (0, wCam), (0, screenW))
        screenY = np.interp(y1, (0, hCam), (0, screenH))

        clocX = plocX + (screenX - plocX) / smoothening
        clocY = plocY + (screenY - plocY) / smoothening

        pyautogui.moveTo(clocX, clocY)

        plocX, plocY = clocX, clocY

        # Check distance between thumb tip (4) and index tip (8)
        length = detector.findDistance(4, 8, img, lmList)

        if length < 30:

            currentTime = time.time()

            if currentTime - lastClick > 0.5:

                pyautogui.click()
                lastClick = currentTime

        cv2.circle(img, (x1, y1), 15,
                   (255, 0, 255),
                   cv2.FILLED)

    cv2.imshow("Virtual Mouse", img)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()