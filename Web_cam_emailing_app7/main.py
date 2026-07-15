import cv2
import time
import os
import glob
from threading import Thread
from emailing import send_email

# Create images folder if it doesn't exist
if not os.path.exists("images"):
    os.makedirs("images")

# Open webcam
video = cv2.VideoCapture(0)

if not video.isOpened():
    print("Error: Could not open webcam.")
    exit()

time.sleep(2)

first_frame = None
status_list = []
count = 1
image_with_object = None


def clean_folder():
    print("Cleaning images folder...")
    images = glob.glob("images/*.png")
    for image in images:
        try:
            os.remove(image)
        except:
            pass
    print("Images folder cleaned.")


while True:

    status = 0

    check, frame = video.read()

    if not check:
        print("Could not read frame.")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    if first_frame is None:
        first_frame = gray
        continue

    delta_frame = cv2.absdiff(first_frame, gray)

    thresh = cv2.threshold(delta_frame, 60, 255, cv2.THRESH_BINARY)[1]
    thresh = cv2.dilate(thresh, None, iterations=2)

    contours, _ = cv2.findContours(
        thresh,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    for contour in contours:

        if cv2.contourArea(contour) < 5000:
            continue

        status = 1

        x, y, w, h = cv2.boundingRect(contour)

        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            3,
        )

        image_with_object = f"images/{count}.png"

        cv2.imwrite(image_with_object, frame)

        count += 1

    status_list.append(status)
    status_list = status_list[-2:]

    if len(status_list) == 2:

        if status_list[0] == 1 and status_list[1] == 0:

            if image_with_object is not None:

                email_thread = Thread(
                    target=send_email,
                    args=(image_with_object,),
                    daemon=True,
                )

                clean_thread = Thread(
                    target=clean_folder,
                    daemon=True,
                )

                email_thread.start()
                email_thread.join()

                clean_thread.start()

    cv2.imshow("Motion Detector", frame)
    cv2.imshow("Threshold", thresh)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()
cv2.destroyAllWindows()