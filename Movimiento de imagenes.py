import cv2
import  numpy as np 
#Leer imagen y reescalar 
imag=cv2.imread('Tarea.jpg',0)
img=cv2.resize(imag,(600,400))

#Copear imagen 
horizontal=imag.copy()
vertical=imag.copy()
ambas=imag.copy()

#Aplicar rotazion de imagen 
horizontal=cv2.flip(img,0)
vertical=cv2.flip(img,1)
ambas=cv2.flip(img,-1)

#Cambiar escala de colores 
imagen1=cv2.imread('aa.jpg',1)
c=cv2.resize(imagen1,(540,1080))
a=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY)
b=cv2.cvtColor(a,cv2.COLOR_GRAY2BGR)

#Mostrar imagenes de rotazion 
cv2.imshow('Original',img)
cv2.imshow('Horizontal',horizontal)
cv2.imshow('Vertical',vertical)
cv2.imshow('Ambas',ambas)
#
cv2.waitKey(0)
cv2.destroyAllWindows()
#Mostrar imagenes de reescalado 
cv2.imshow('C',c)
cv2.imshow('A',a)
cv2.imshow('B',b)
#
cv2.waitKey(0)
cv2.destroyAllWindows()

#Aplicar umbral 
imagen_G=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY)
lim_min=90
Color=255
_, umbralSimple=cv2.threshold(imagen_G,lim_min,Color,cv2.THRESH_BINARY)

#mostrar imagenes con umbral 
cv2.imshow("Imagen Original",c)
cv2.imshow("Imagen con Umbrel",umbralSimple)
#
cv2.waitKey(0)
cv2.destroyAllWindows()
