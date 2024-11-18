import cv2
import numpy as np

ig=cv2.imread("image3.jpg")
h, w, c=ig.shape

convo=np.zeros((h,w,c), np.uint8)
kernel=np.array([[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])
#print(kernel.shape)
hk=kernel.shape[0]//2
wk=kernel.shape[1]//2

for fila in range(hk,h-wk):
    for columna in range(wk,w-wk):
        acumulador=0
        for i in range(kernel.shape[0]):
            for j in range(kernel.shape[1]):
                acumulador+=(kernel[i,j]*ig[fila+(i-hk),columna+(j-wk)])

        convo[fila,columna]=np.clip(acumulador,0,255).astype('uint8')



cv2.imshow("Imagen random",ig)
cv2.imshow("Imagen convolucionada",convo)
cv2.waitKey()