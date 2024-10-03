import cv2
import numpy as np
import matplotlib.pyplot as plt

image =cv2.imread("Goku.jpg")

image = cv2.resize(image, (0,0), fx=0.4, fy=0.4)

gussian_blur = cv2.GaussianBlur(image, (5,5),0)

median_blur = cv2.medianBlur(image, 5)

bilateral_blur = cv2.bilateralFilter(image, 0, 75, 75)

Titulos = ["Original", "Desenfoque Gausiano", "Desenfoque mediano", "desenfoque bilateral", "sobel", "canny"]

imagenes = [image, gussian_blur, median_blur, bilateral_blur]


for i in range(4):
	plt.subplot(2,2,i + 1)
	plt.title(Titulos[i])
	plt.imshow(cv2.cvtColor(imagenes[i], cv2.COLOR_BGR2RGB))
	plt.xticks([]), plt.yticks([])
plt.tight_layout()
plt.show()