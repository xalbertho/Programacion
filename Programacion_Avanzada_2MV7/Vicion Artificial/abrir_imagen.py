import cv2, numpy as np
image=cv2.imread("Imagen1.png")

h,w,c=image.shape
img2=np.zeros((h,w,c),np.uint8)
im3=np.zeros((h,w,c),np.uint8)

for f in range(h):
    for c in range(w):
        pixel=image[f,c]
        prom=sum(pixel)//3
        #print(image[f,c])
        img2[f,c]=[prom,prom,prom]

        BRI=np.clip(pixel+100,0,255).astype('uint8')
        im3=BRI




cv2.imshow("COPIA DE LA IMAGEN",im3)
cv2.waitKey()
cv2.imshow("COPIA DE LA IMAGEN",img2)
cv2.waitKey()


#cv2.imshow("Captura",image)
#cv2.waitKey()