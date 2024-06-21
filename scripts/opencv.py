import cv2

carrega = cv2.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
img = cv2.imread("imagens/imagen7.jpg")
imagen_cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rostos = carrega.detectMultiScale(imagen_cinza)
print(rostos)

for(x, y, l, a) in rostos:
    cv2.rectangle(img, (x, y), (x + l, y + l), (0, 255, 0), 1)

cv2.imshow("rostos", img)
cv2.waitKey()


