import cv2
import os
import time
from threading import Thread
from ultralytics import YOLO
from emailing import send_email


# Create image folder

if not os.path.exists("images"):
    os.makedirs("images")



# Load YOLO model

print("Loading AI model...")

model = YOLO("yolov8n.pt")

print("Model loaded!")



# Open camera

camera = cv2.VideoCapture(0)


if not camera.isOpened():

    print("Camera not found")
    exit()



time.sleep(2)



image_count = 1

person_detected_before = False



while True:


    success, frame = camera.read()


    if not success:
        break



    # YOLO detection

    results = model(
        frame,
        conf=0.5,
        verbose=False
    )


    person_detected = False



    for result in results:


        boxes = result.boxes


        for box in boxes:


            class_id = int(box.cls[0])


            confidence = float(box.conf[0])


            # YOLO class 0 = person

            if class_id == 0 and confidence > 0.5:


                person_detected = True


                x1,y1,x2,y2 = map(
                    int,
                    box.xyxy[0]
                )


                cv2.rectangle(
                    frame,
                    (x1,y1),
                    (x2,y2),
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



    # Send email only once when person appears

    if person_detected and not person_detected_before:


        image_path = f"images/intruder_{image_count}.jpg"


        cv2.imwrite(
            image_path,
            frame
        )


        print(
            "Person detected:",
            image_path
        )


        email_thread = Thread(
            target=send_email,
            args=(image_path,)
        )


        email_thread.start()



        image_count += 1



    person_detected_before = person_detected



    cv2.imshow(
        "AI Security Camera",
        frame
    )


    key = cv2.waitKey(1)


    if key == ord("q"):
        break



camera.release()

cv2.destroyAllWindows()