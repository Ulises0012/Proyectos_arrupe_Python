import cv2

class DeteccionForma:
    def __inin__(self):
        pass
    def detectar(self, c):
        shape = "sin definir"
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) ==3:
            shape = "Triángulo"
        elif len(approx) ==4:
            (x,y,w,h) = cv2.boundingRect(approx)
            ar = w/float(h)
            shape = "cuadrado" if ar >= 0.95 and ar <= 1.05 else "Rectangulo"
        elif len(approx) ==5:
            shape = "Pentangono"
        else:
            shape = "circulo"
        return shape