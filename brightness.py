import cv2
import numpy as np
import math
from cvzone.HandTrackingModule import HandDetector
import screen_brightness_control as sbc

cap=cv2.VideoCapture(0)
detector=HandDetector(detectionCon=0.7, maxHands=1)

control_active=False

while True:
    success, img=cap.read()
    if not success:
        break

    img=cv2.flip(img, 1)
    hands, img=detector.findHands(img)

    if hands and control_active:
        hand=hands[0]
        lmList=hand["lmList"]

        x1, y1=lmList[4][0], lmList[4][1]
        x2, y2=lmList[8][0], lmList[8][1]

        length=math.hypot(x2-x1, y2-y1)
        brightness=int(np.interp(length, [30, 200], [0, 100]))
        sbc.set_brightness(brightness)

    status="ACTIVE" if control_active else "PAUSED"

    cv2.rectangle(img, (10, 10), (420, 90), (0, 0, 0), -1)
    cv2.putText(img, "MODE: BRIGHTNESS", (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    cv2.putText(img, f"STATUS: {status}", (20, 75),
                cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 255), 2)
    
    cv2.imshow("Hand Gesture Brightness Control", img)

    key=cv2.waitKey(1) & 0xFF

    if key==ord("s"):
        control_active=True
    elif key==ord("p"):
        control_active=False
    elif key==ord("q"):
        break

cap.release()
cv2.destroyAllWindows()