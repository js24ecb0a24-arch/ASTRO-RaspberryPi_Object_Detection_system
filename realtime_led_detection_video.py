import cv2
import RPi.GPIO as GPIO
import threading
import subprocess
from picamera2 import Picamera2
from ultralytics import YOLO

# ==============================
# GPIO SETUP
# ==============================
GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

# ==============================
# CAMERA SETUP
# ==============================
picam2 = Picamera2()
picam2.preview_configuration.main.size = (320, 320)
picam2.preview_configuration.main.format = "RGB888"
picam2.preview_configuration.align()
picam2.configure("preview")
picam2.start()

# ==============================
# LOAD YOLO MODEL
# ==============================
model = YOLO("models/yolov8n.pt")

# ==============================
# VIDEO OUTPUT SETUP
# ==============================
output_path = "output/detection_output.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
fps = 10
out = cv2.VideoWriter(output_path, fourcc, fps, (320, 320))

# ==============================
# FRAME SKIPPING
# ==============================
frame_skip = 4
frame_count = 0
person_detected = False

# ==============================
# LED THREAD
# ==============================
def led_worker():
    global person_detected

    while True:
        GPIO.output(
            LED_PIN,
            GPIO.HIGH if person_detected else GPIO.LOW
        )

led_thread = threading.Thread(target=led_worker, daemon=True)
led_thread.start()

# ==============================
# MAIN LOOP
# ==============================
try:
    while True:
        frame = picam2.capture_array()

        frame_count += 1

        if frame_count % frame_skip != 0:
            continue

        frame = cv2.resize(frame, (320, 320))

        # PERSON DETECTION ONLY
        results = model(frame, classes=[0])

        boxes = results[0].boxes

        person_detected = len(boxes) > 0

        annotated_frame = results[0].plot()

        out.write(annotated_frame)

        cv2.imshow("ASTRo Detection", annotated_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Program interrupted.")

finally:
    picam2.stop()
    out.release()
    cv2.destroyAllWindows()

    GPIO.output(LED_PIN, GPIO.LOW)
    GPIO.cleanup()

    print("Uploading video to Google Drive...")

    subprocess.run([
        "rclone",
        "copy",
        output_path,
        "gdrive:/ASTRoUploads/"
    ])

    print("Upload complete.")
