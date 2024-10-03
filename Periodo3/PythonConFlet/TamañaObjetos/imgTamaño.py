from scipy.spatial import distance as dist
from imutils import perspective
from imutils import contours
import numpy as np
import imutils
import cv2

def midpoint(ptA, ptB):
    return ((ptA[0] + ptB[0]) * 0.5, (ptA[1] + ptB[1]) * 0.5)

def process_image(image_path, object_width, side):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    edged = cv2.Canny(gray, 30, 150)
    edged = cv2.dilate(edged, None, iterations=1)
    edged = cv2.erode(edged, None, iterations=1)

    cnts = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    (cnts, _) = contours.sort_contours(cnts)
    pixelsPerMetric = None
    processed_image_path = "processed_image.jpg"
    
    for c in cnts:
        if cv2.contourArea(c) < 500:
            continue
        
        orig = image.copy()
        box = cv2.minAreaRect(c)
        box = cv2.boxPoints(box) if imutils.is_cv4() else cv2.cv.BoxPoints(box)
        box = np.array(box, dtype="int")
        box = perspective.order_points(box)

        cv2.drawContours(orig, [box.astype("int")], -1, (0, 255, 0), 2)

        # Calcular dimensiones en la imagen
        (tl, tr, br, bl) = box
        (tl_br_dist, tl_tr_dist, tr_br_dist) = (dist.euclidean(tl, br), dist.euclidean(tl, tr), dist.euclidean(tr, br))
        width = tl_tr_dist if side == "Left" else tl_br_dist
        height = tl_br_dist if side == "Left" else tl_tr_dist

        if pixelsPerMetric is None:
            pixelsPerMetric = width / object_width

        # Mostrar medidas en la imagen
        cv2.putText(orig, f"Width: {width / pixelsPerMetric:.2f} cm", (int(tl[0]), int(tl[1] - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        cv2.putText(orig, f"Height: {height / pixelsPerMetric:.2f} cm", (int(tl[0]), int(tl[1] - 30)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

        # Mostrar área y contorno
        area = cv2.contourArea(c)
        cv2.putText(orig, f"Area: {area:.2f}", (int(tl[0]), int(tl[1] - 50)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

    # Guardar la imagen procesada
    cv2.imwrite(processed_image_path, orig)

    return processed_image_path
