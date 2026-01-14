import cv2
import serial
import time

ser = serial.Serial('COM5', 9600)
time.sleep(2)

face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)
eye_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_eye.xml'
)

cap = cv2.VideoCapture(0)

ALERT_TIME = 0.2
eyes_closed_start = None
last_sent = None

def send(cmd):
    global last_sent
    if cmd != last_sent:
        ser.write(cmd.encode())
        last_sent = cmd

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    eyes_open = False
    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
        if len(eyes) > 0:
            eyes_open = True
            break

    if eyes_open:
        eyes_closed_start = None
        send('G')
        cv2.putText(frame, "EYES OPEN", (30, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    else:
        if eyes_closed_start is None:
            eyes_closed_start = time.time()

        elapsed = time.time() - eyes_closed_start

        if elapsed >= ALERT_TIME:
            send('R')
            cv2.putText(frame, "SLEEP ALERT", (30, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
        else:
            cv2.putText(frame, "EYES CLOSED", (30, 40),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,255), 2)

    cv2.imshow("Driver Drowsiness Detection", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
ser.close()