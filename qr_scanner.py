import cv2
from datetime import datetime

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = cv2.QRCodeDetector()

last_data = ""

print("QR Code Scanner Started")
print("Show a QR code to the camera")
print("Press Q to exit")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Camera could not be opened.")
        break

    data, points, _ = detector.detectAndDecode(frame)

    # QR Code found
    if points is not None and data:
        points = points.astype(int)

        # Green box
        for i in range(4):
            cv2.line(
                frame,
                tuple(points[0][i]),
                tuple(points[0][(i + 1) % 4]),
                (0, 255, 0),
                3
            )

        cv2.putText(
            frame,
            "QR Code Detected!",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 255, 0),
            2
        )

        cv2.putText(
            frame,
            data[:50],
            (20, 80),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2
        )

        if data != last_data:
            print("\nQR Code Detected!")
            print("Data:", data)
            print("Time:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            last_data = data

    # No QR Code
    else:
        last_data = ""

        cv2.putText(
            frame,
            "No QR Code Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (0, 0, 255),
            2
        )

    # Show camera
    cv2.imshow("QR Code Scanner", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

print("QR Scanner Closed.")