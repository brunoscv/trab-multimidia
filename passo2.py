import numpy as np
import cv2
#import mahotas


def escreve(img, texto, cor=(255, 0, 0)):
    fonte = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(img, texto, (10, 20), fonte, 0.5, cor, 0,
                cv2.LINE_AA)

imgColorida = cv2.imread('dados.jpeg')

#Passo 2: Blur/Suavização da imagem
suave = cv2.blur(imgColorida, (7, 7))
escreve(suave, "Suavizacao com Blur", 0)

temp = np.vstack([
    np.hstack([suave])
])

cv2.imshow("Resultado", suave)
cv2.waitKey(0)