import numpy as np
import cv2
import mahotas


def escreve(img, texto, cor=(255, 0, 0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10, 20), fonte, 0.5, cor, 0,
                cv2.LINE_AA)


imgColorida = cv2.imread('dados.jpeg')
suave = cv2.blur(imgColorida, (7, 7))

# Passo 3: Binarização resultando em pixels brancos e pretos
T = mahotas.thresholding.otsu(suave)
bin = suave.copy()
bin[bin > T] = 255
bin[bin < 255] = 0
bin = cv2.bitwise_not(bin)

escreve(bin, "Binarizacao com Metodo Otsu", 255)

temp = np.vstack([
    np.hstack([bin])
])

cv2.imshow("Resultado", bin)
cv2.waitKey(0)
