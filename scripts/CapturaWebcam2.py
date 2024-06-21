import cv2

webCamera = cv2.VideoCapture(0)
classificador_face = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
classificador_olho = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")

while True:
    camera, frame = webCamera.read()
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    detecta = classificador_face.detectMultiScale(cinza, scaleFactor=1.03, minNeighbors=3, minSize=(20, 20))
    for(x, y, l, a) in detecta:
        cv2.rectangle(frame, (x, y), (x + l, y + a), (255, 0, 255), 1)
        pegaOlho = frame[y:y + a, x:x + l]
        olho_cinza = cv2.cvtColor(pegaOlho, cv2.COLOR_BGR2GRAY)
        localizaOlho = classificador_olho.detectMultiScale(olho_cinza, scaleFactor=1.10, minNeighbors=7, minSize=(20,20))
        for (ox, oy, ol, oa) in localizaOlho:
            cv2.rectangle(pegaOlho, (ox, oy), (ox + ol, oy + oa), (255, 255, 0), 1)
    cv2.imshow("Video WebCamera", frame)
    if cv2.waitKey(1) == ord("q"):
        break

webCamera.release()
cv2.destroyWindow("Video WebCamera")
