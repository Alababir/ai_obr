import cv2

webCam = cv2.VideoCapture(0)
carrega_eye = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")
Classificador = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")

while True:
    camera, frame = webCam.read()
    filmagem_cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    descobre = Classificador.detectMultiScale(filmagem_cinza, scaleFactor=1.8, minNeighbors=2, minSize=(10, 10))


    for (x, y, l, a) in descobre:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 255), 1)

    cv2.imshow("Imagen camera", frame)

    if cv2.waitKey(1) == ord("q"):
        break

webCam.release()
cv2.destroyAllWindows()