import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("Goku.jpg")

image_rbg = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

edges = cv2.Canny(image = image_rbg, threshold1=80, threshold2=255)

fig, axs = plt.subplots(1,2,figsize=(7,4))

axs[0].imshow(image_rbg)
axs[0].set_title("Imagen original")


axs[1].imshow(edges)
axs[1].set_title("Imagenn edges")

for ax in axs:
	ax.set_xticks([])

	ax.set_yticks([])
plt.tight_layout()
plt.show()