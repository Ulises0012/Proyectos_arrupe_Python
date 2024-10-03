import cv2

cargar_gatos_Harr = cv2.CascadeClassifier('haarcascade_frontalcatface_extended.xml')

image = cv2.imread('dogs_and_cats.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gatos = cargar_gatos_Harr.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=10, minSize=(30,30), maxSize=(100,100))

for (x,y,w,h) in gatos:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 0), 2)
    
cv2.imshow("Rsotros de gatos", image)
cv2.waitKey(0)
cv2.destroyAllWindows()