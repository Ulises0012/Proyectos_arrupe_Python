from skimage.metrics import structural_similarity as compare_ssim
import argparse
import imutils
import cv2

imageA = cv2.imread("comparacion_tarjetas.jpg")

imageB = cv2.imread("comparacion_tarjetas2.jpg")

grayA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)

grayB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)

(score, diff) = compare_ssim(grayA, grayB, full=True)
diff = (diff *255).astype("uint8")
print("SSIM: {}".format(score))

thresh = cv2.threshold(diff, 0,255,cv2.THRESH_BINARY_INV|cv2.THRESH_OTSU)[1]
cv2.imshow("Primera imagen", imageA)
cv2.imshow("Segunda imagen", imageB)
cv2.imshow("Diferencia entre las imagenes", diff)
cv2.imshow("Regiones de Diferencia", thresh)
cv2.waitKey(0)