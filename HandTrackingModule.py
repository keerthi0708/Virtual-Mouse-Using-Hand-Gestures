import cv2
import mediapipe as mp
import math

class handDetector:

    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img):

        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:

            for handLms in self.results.multi_hand_landmarks:

                self.mpDraw.draw_landmarks(
                    img,
                    handLms,
                    self.mpHands.HAND_CONNECTIONS
                )

        return img

    def findPosition(self, img):

        lmList = []

        if self.results.multi_hand_landmarks:

            hand = self.results.multi_hand_landmarks[0]

            for id, lm in enumerate(hand.landmark):

                h, w, c = img.shape

                cx = int(lm.x * w)
                cy = int(lm.y * h)

                lmList.append([id, cx, cy])

        return lmList

    def findDistance(self, p1, p2, img, lmList):

        x1, y1 = lmList[p1][1:]
        x2, y2 = lmList[p2][1:]

        cv2.line(img, (x1, y1), (x2, y2),
                 (255, 0, 255), 2)

        cv2.circle(img, (x1, y1), 8,
                   (255, 0, 255), cv2.FILLED)

        cv2.circle(img, (x2, y2), 8,
                   (255, 0, 255), cv2.FILLED)

        length = math.hypot(x2 - x1, y2 - y1)

        return length