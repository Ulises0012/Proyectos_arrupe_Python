from scipy.spatial import distance as dist 
from imutils import perspective
from imutils import contours
import numpy as np
import argparse
import imutils
import cv2

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="ruta a la imagen de entrada")
ap.add_argument("-w", "--width", type=float, required=True, help="ancho del objeto más a la izquierda en la imagen (en cm)") 
args = vars(ap.parse_args())

image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (7, 7), 0)

edged = cv2.Canny(gray, 50, 100)
edged = cv2.dilate(edged, None, iterations=1) 
edged = cv2.erode(edged, None, iterations=1)

cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
(cnts, _) = contours.sort_contours(cnts)
pixelsPerMetric = None

for c in cnts:
    if cv2.contourArea(c) < 100:
        continue

    orig = image.copy()
    box = cv2.minAreaRect(c)
    box = cv2.boxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
    box = np.array(box, dtype="int")

    box = perspective.order_points(box)
    cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

    (tl, tr, br, bl) = box
    (tltrx, tltry) = midpoint(tl, tr)
    (blbrx, blbry) = midpoint(bl, br)
    (tlblx, tlbly) = midpoint(tl, bl)
    (trbrx, trbry) = midpoint(tr, br)

    cv2.circle(orig, (int(tltrx), int(tltry)), 5, (255, 0, 0), -1) 
    cv2.circle(orig, (int(blbrx), int(blbry)), 5, (255, 0, 0), -1) 
    cv2.circle(orig, (int(tlblx), int(tlbly)), 5, (255, 0, 0), -1) 
    cv2.circle(orig, (int(trbrx), int(trbry)), 5, (255, 0, 0), -1)

    dA = dist.euclidean((tltrx, tltry), (blbrx, blbry))
    dB = dist.euclidean((tlblx, tlbly), (trbrx, trbry))

    if pixelsPerMetric is None:
        pixelsPerMetric = dB / args["width"]

    dimA = dA / pixelsPerMetric
    dimB = dB / pixelsPerMetric

    cv2.putText(orig, "{:.1f}cm".format(dimA),
                (int(tltrx - 15), int(tltry - 10)), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (255, 255, 255), 2)
    cv2.putText(orig, "{:.1f}cm".format(dimB),
                (int(trbrx + 10), int(trbry)), cv2.FONT_HERSHEY_SIMPLEX,
                0.65, (255, 255, 255), 2)

    cv2.imshow("Image", orig)
    cv2.waitKey(0)
    