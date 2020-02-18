import cv2
import matplotlib.pyplot as plt

img = cv2.imread('./image/cat.jpg', cv2.IMREAD_COLOR)
img2 = cv2.imread('./image/cat.jpg', cv2.IMREAD_COLOR)

plt.imshow(img, interpolation='bicubic')
plt.imshow(img2[:,:,::-1], interpolation='bicubic')
plt.xticks([])
plt.yticks([])
plt.show()