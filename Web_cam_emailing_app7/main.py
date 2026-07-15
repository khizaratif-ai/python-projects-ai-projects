import cv2
import os
import time
from threading import Thread
from ultralytics import YOLO
from emailing import send_email


# Create images folder
if not os.path.exists("images"):
    os.makedirs("images")


print("Loading AI model...")
model = YOLO("yolov8n.pt")
print("Model loaded!")


camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera not found")
    exit()


time.sleep(2)


# Security settings
image_taken = False
last_person_time = 0

# Time person must be gone before resetting
RESET_TIME = 10   # seconds


image_number = 1



while True:

    success, frame = camera.read()

    if not success:
        break


    results = model(
        frame,
        conf=0.5,
        verbose=False
    )


    person_detected = False



    for result in results:

        for box in result.boxes:

            class_id = int(box.cls[0])
            confidence = float(box.conf[0])


            # YOLO class 0 = person

            if class_id == 0 and confidence > 0.5:

                person_detected = True


                x1, y1, x2, y2 = map(
                    int,
                    box.xyxy[0]
                )


                cv2.rectangle(
                    frame,
                    (x1, y1),
                    (x2, y2),
                    (0,255,0),
                    3
                )


                cv2.putText(
                    frame,
                    f"Person {confidence:.2f}",
                    (x1,y1-10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0,255,0),
                    2
                )



    # Person detected

    if person_detected:


        last_person_time = time.time()


        # Take only one picture

        if not image_taken:


            image_path = f"images/intruder_{image_number}.jpg"


            cv2.imwrite(
                image_path,
                frame
            )


            print(
                "Image captured:",
                image_path
            )


            email_thread = Thread(
                target=send_email,
                args=(image_path,)
            )


            email_thread.start()


            image_number += 1


            image_taken = True




    # Person disappeared

    if not person_detected:


        if image_taken:


            time_difference = (
                time.time() - last_person_time
            )


            # Reset after person leaves

            if time_difference > RESET_TIME:


                print(
                    "System ready for new detection"
                )


                image_taken = False




    cv2.imshow(
        "AI Security Camera",
        frame
    )


    key = cv2.waitKey(1)


    if key == ord("q"):
        break



camera.release()
cv2.destroyAllWindows()