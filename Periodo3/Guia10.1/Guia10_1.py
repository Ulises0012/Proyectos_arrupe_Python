import numpy as np
import argparse
import imutils
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, default="figura.png", help="path to input image")
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
cv2.imshow("Figura", image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 200,255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("Imagen umbralizada", thresh)
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
c = max(cnts, key = cv2.contourArea)
output = image.copy()
cv2.drawContours(output, [c], -1, (128,0,0),3)
(x,y,w,h) = cv2.boundingRect(c)
text = "Original, puntos ={}".format(len(c))
cv2.putText(output, text,(x,y -5), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(128.0,0),2)
print("[INFO] {}".format(text))
cv2.imshow("Contorno original (Todos los puntod)",output)
cv2.waitKey(0)

for eps in np.linspace(0.001,0.05,10):
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, eps * peri, True)
    output = image.copy()
    cv2.drawContours(output, [approx], -1, (128,0,0),3)
    text = "eps={:.4f}, puntos={}".format(eps, len(approx))
    cv2.putText(output, text, (x,y -5), cv2.FONT_HERSHEY_SIMPLEX, 0.9,(128,0,0),2)
    print("[INFO] {}".format(text))
    cv2.imshow("Aproximacion de contornos", output)
    cv2.waitKey(0)
    