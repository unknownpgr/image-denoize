import numpy as np

import cv2

cap = cv2.VideoCapture("TestFile1.mp4")

# Convert frame type to float64
img = np.array(cv2.cvtColor(cap.read()[1], cv2.COLOR_BGR2GRAY), np.float64)
count = 1

while cap.isOpened():

    ret, frame = cap.read()

    if not ret:
        break

    if count % 100 is 0:
        print('processed frame :', count)

    # Add frame
    img += cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    count += 1

cap.release()


# Convert image value range into 0-255
def image_into_range(img):
    result = img * (255 / np.max(img))
    return result


img = image_into_range(img)
img = np.array(img, np.uint8)
cv2.imwrite('./result.jpg', img)
