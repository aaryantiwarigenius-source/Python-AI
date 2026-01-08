import cv2
import numpy as np

cap=cv2.VideoCapture(0)
current_mode='original'
gaussian_kernel=5
median_kernel=5

while True:
    ret, frame=cap.read()
    if not ret:
        break

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    output=frame.copy()

    if current_mode=='laplacian':
        lap=cv2.Laplacian(gray, cv2.CV_64F)
        output=cv2.cvtColor(np.uint8(np.absolute(lap)), cv2.COLOR_GRAY2BGR)

    elif current_mode=='gaussian':
        if gaussian_kernel % 2 ==0:
            gaussian_kernel +=1
        output=cv2.GaussianBlur(frame, (gaussian_kernel, gaussian_kernel), 0)

    cv2.imshow("Live Filter Detection", output)

    key=cv2.waitKey(1) & 0xFF
    if key==ord('q'):
        break
    elif key==ord('g'):
        current_mode='gaussian'
    elif key==ord('l'):
        current_mode='laplacian'
    elif key==ord('o'):
        current_mode='original'

cap.release()
cv2.destroyAllWindows()