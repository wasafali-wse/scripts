import cv2

# Open the camera (0 is usually the default camera, use a valid RTSP URL if using an IP camera)
# For USB Camera
# cap = cv2.VideoCapture(0)
#"rtsp://admin:wheed1118@192.168.100.125:554/cam/realmonitor?channel=2&subtype=0"
# For IP Camera (replace with your actual stream URL)
cap = cv2.VideoCapture('rtsp://admin:wheed1118@192.168.100.125:554/cam/realmonitor?channel=2&subtype=0')

if not cap.isOpened():
    print("Error: Unable to open the camera.")
    exit()

while True:
    ret, frame = cap.read()
    
    if not ret:
        print("Error: Unable to read frame.")
        break

    cv2.imshow('Camera Feed', frame)

    key = cv2.waitKey(1)
    
    # Press 'c' to capture the image
    if key & 0xFF == ord('c'):
        cv2.imwrite('captured_image.jpg', frame)
        print("Image captured and saved as 'captured_image.jpg'.")

    # Press 'q' to quit
    elif key & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()