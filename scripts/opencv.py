import cv2

carrega = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("imagens/imagen1.jpg")
imagen_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rostos = carrega.detectMultiScale(imagen_cinza)
print(rostos)
cv2.imshow("rostos", img)
cv2.waitKey()
