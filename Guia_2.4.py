import cv2
import numpy as np

image1 = cv2.imread("Goku.jpg")
image2 = cv2.imread("FlorColores.jpg")

image2_resize = cv2.resize(image2, (image1.shape[1], image1.shape[0]))
weigtedSum = cv2.addWeighted(image1, 0.7, image2_resize, 0.3,0)

cv2.imshow("imagen ponderada", weigtedSum)
if cv2.waitKey(0):
	cv2.destroyAllWindows()
