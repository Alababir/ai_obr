import cv2

carrega_face = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")  # arquivos rosto
carrega_eye = cv2.CascadeClassifier("haarcascades/haarcascade_eye.xml")  # arquivos olhos

img = cv2.imread("imagens/imagen10.jpg")  # abre o arquivo
imagen_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # transforma a imagem em um gradiente cinza
rostos = carrega_face.detectMultiScale(imagen_cinza, scaleFactor=1.05, minNeighbors=3, minSize=(20, 20))

for (x, y, l, a) in rostos:  # lopp para detectar rostos
    img = cv2.rectangle(img, (x, y), (x + l, y + l), (255, 0, 255), 1)
    Localolho = img[y:y + a, x:x + l]
    Lolho_cinza = cv2.cvtColor(Localolho, cv2.COLOR_BGR2GRAY)
    detectado = carrega_eye.detectMultiScale(Lolho_cinza, minSize=(10, 10), minNeighbors=5, scaleFactor=1.05)


for (ox, oy, ol, oa) in detectado:  # loop para detectar olos dentro dos rostos
    cv2.rectangle(Localolho, (ox, oy), (ox + ol, oy + ol), (255, 255, 0), 1)


cv2.imshow("Dalhe rosto e olhos ", img)
cv2.waitKey()
