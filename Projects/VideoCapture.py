import cv2
video_cap = cv2.videoCapture(0)
while True:
    ret, video = video_cap.read()
    cv2.immshow("video_live")