import cv2
import numpy as np
import matplotlib.pyplot as plt

image =cv2.imread("Goku.jpg")

decima = cv2.resize(image, (0,0), fx=0.1, fy=0.1)

brigger = cv2.resize(image, (6000,3500))

interpolacion = cv2.resize(image, (780,540), interpolation= cv2.INTER_LINEAR)

Titulos = ["Original", "Decima parte original", "Más grande", "Interpolación Lineal"]

imagenes = [image, decima, brigger, interpolacion]
cantidad = 4

for i in range(cantidad):
	plt.subplot(2,2,i + 1)
	plt.title(Titulos[i])
	plt.imshow(cv2.cvtColor(imagenes[i], cv2.COLOR_BGR2RGB))

plt.show()