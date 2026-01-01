import cv2

cap=cv2.VideoCapture(0)

show_rect=False
show_center=False
show_line=False
show_height=False

while True:
    ret, frame=cap.read()
    if not ret:
        break

    height, width, _ = frame.shape

    rect1_w, rect1_h=150, 150
    rect2_w, rect2_h=200, 150

    top_left1=(20, 20)
    bottom_right1 = (20 + rect1_w, 20 + rect1_h)

    top_left2 = (width - rect2_w - 20, height - rect2_h - 20)
    bottom_right2 = (top_left2[0] + rect2_w, top_left2[1] + rect2_h)

    center1 = (top_left1[0] + rect1_w // 2, top_left1[1] + rect1_h // 2)
    center2 = (top_left2[0] + rect2_w // 2, top_left2[1] + rect2_h // 2)

    if show_rect:
        cv2.rectangle(frame, top_left1, bottom_right1, (0, 255, 255), 3)
        cv2.rectangle(frame, top_left2, bottom_right2, (255, 0, 255), 3)
        cv2.putText(frame, "Region 1", (top_left1[0], top_left1[1] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)
        cv2.putText(frame, "Region 2", (top_left2[0], top_left2[1] - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,255), 2)

    if show_center:
        cv2.circle(frame, center1, 15, (0, 255, 0), -1)
        cv2.circle(frame, center2, 15, (0, 0, 255), -1)
        cv2.putText(frame, "C1", (center1[0]-20, center1[1]+35),
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,255,0), 2)
        cv2.putText(frame, "C2", (center2[0]-20, center2[1]+35),
        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,255), 2)

    if show_line:
        cv2.line(frame, center1, center2, (0, 255, 0), 3)

    if show_height:
        arrow_start=(width - 50, 20)
        arrow_end=(width - 50, height - 20)

        cv2.arrowedLine(frame, arrow_start, arrow_end, (255, 255, 0), 3, tipLength=0.05)
        cv2.arrowedLine(frame, arrow_end, arrow_start, (255, 255, 0), 3, tipLength=0.05)
       
        cv2.putText(frame, f"Height: {height}px",
                    (width - 250, height // 2),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)
        
    cv2.imshow("Live Annotation", frame)

    key=cv2.waitKey(1) & 0xFF
    if key==ord('r'):
        show_rect = not show_rect
    elif key==ord('c'):
        show_center=not show_center
    elif key==ord('l'):
        show_line=not show_line
    elif key==ord('h'):
        show_height = not show_height
    elif key==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()