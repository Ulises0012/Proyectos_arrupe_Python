from  clase_detector_formas import DeteccionForma
import argparse
import imutils
import cv2
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="ruta a la imagen de entrada")
args = vars(ap.parse_args())
image = cv2.imread(args["image"])
resized = imutils.resize(image, width=300)
ratio = image.shape[0]/float(resized.shape[0])
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)[1]
cnts = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
sd = DeteccionForma()
for c in cnts:
    M = cv2.moments(c)
    cX = int((M["m10"]/M["m00"]) * ratio)
    cY = int((M["m01"] / M["m00"]) * ratio)
    shape = sd.detectar(c)
    c = c.astype("float")
    c *= ratio
    c= c.astype("int")
    area = cv2.contourArea(c)
    print(f"Área del {shape}: {area}")
    (x,y,w,h) = cv2.boundingRect(c)
    print(f"Ancho del {shape}: {w}")
    print(f"Alto del {shape}: {h}")
    
cv2.imshow("Image", image)
cv2.waitKey(0)
