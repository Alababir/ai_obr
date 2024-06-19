import cv2

webcam = cv2.VideoCapture(0)

while True:
    camera, frame = webcam.read()

    cv2.imshow("Imagen Webcamera", frame)

    if cv2.waitKey(1) == ord("q"):
        break

webcam.release()
cv2.destryAllWindows()
