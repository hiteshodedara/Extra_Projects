# beta version program
# this program take some changes to good output...

import cv2  # for image control
from PIL import Image  # for save Image
import time  # for work with time

# for capture video for make pdf page
cap = cv2.VideoCapture(2)

while True:
    # read a video capture
    _, frame = cap.read()

    # Change color of image for good capture
    frame_cnv = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # for a make image smooth
    frame_blur = cv2.GaussianBlur(frame_cnv, (5, 5), 0)

    # for track a image edge
    frame_edge = cv2.Canny(frame_blur, 30, 50)

    # for a take best edges in image
    contours, h = cv2.findContours(frame_edge, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    if contours:
        # for a take max contours
        max_contour = max(contours, key=cv2.contourArea)

        # for make boudoirs for image capture
        x, y, w, h = cv2.boundingRect(max_contour)

        # condition for max contours show in image
        if cv2.contourArea(max_contour) > 5000:

            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)

            object_only = frame[y:y + h, x:x + w]
            # for a output
            cv2.imshow('pdf scanner', object_only)
            if cv2.waitKey(1) == ord('s'):  # save image with s button
                img_pil = Image.fromarray(object_only)

                # for a time
                time_str = time.strftime('%Y-%m-%d-%H-%M-%S')

                # for save image in local disk
                img_pil.save(f'image{time_str}.pdf')
                print('save')
