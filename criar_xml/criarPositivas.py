import cv2
import os
from imutils import paths
import shutil

def ListaNegImagem():
    imagemPath = list(paths.list_images("imagens/comMascara"))
    numero = 1
    if not os.path.exists("pos"):
        os.makedirs("pos")

    for i in imagemPath:
        i.replace(i, "pos/"+str(numero)+".png")
        shutil.copy(i, i.replace(i, "pos/"+str(numero) + ".png"))
        img = cv2.imread("pos/" + str(numero) + ".png", cv2.IMREAD_GRAYSCALE)
        resized_image = cv2.resize(img, (100, 100))
        cv2.imwrite("pos/" + str(numero) + ".png", resized_image)

        print(i.replace(i, "pos/" + str(numero)+ ".png"))

        numero += 1

ListaNegImagem()