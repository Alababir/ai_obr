import cv2

webcam = cv2.VideoCapture(0)
carrega = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
video_cinza = cv2.cvtColor(webcam, cv2.COLOR_BGR2GRAY)

rostos = carrega.detectMultiScale(video_cinza)

print(rostos)

for(x, y, l, a) in rostos:
    cv2.rectangle(webcam, (x, y), (x + l, y + l), (255, 0, 255), 1)

while True:
    camera, frame = webcam.read()

    cv2.imshow("Imagen Webcamera", frame)

    if cv2.waitKey(1) == ord("q"):
        break

webcam.release()
cv2.destryAllWindows()
