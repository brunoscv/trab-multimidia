import numpy as np
import cv2
#import mahotas


def escreve(img, texto, cor=(255, 0, 0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10, 20), fonte, 0.5, cor, 0,
                cv2.LINE_AA)

imgColorida = cv2.imread('dados.jpeg')

# Passo 1: Conversão para tons de cinza
img = cv2.cvtColor(imgColorida, cv2.COLOR_BGR2GRAY)
escreve(img, "Imagem em tons de cinza", 0)

temp = np.vstack([
    np.hstack([img])
])

imgC2 = imgColorida.copy()
cv2.imshow("Imagem Original", imgColorida)
cv2.imshow("Resultado", img)
cv2.waitKey(0)