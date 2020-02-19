import cv2

print(cv2.__version__)

img = cv2.imread('./image/geo.jpg', cv2.IMREAD_UNCHANGED)
#print('type(img) =', type(img))
#print('img.shape, img.dtype =', img.shape, img.dtype)
cv2.imshow('img', img)


img2 = cv2.imread('./image/geo.jpg', cv2.IMREAD_GRAYSCALE)
#print('type(img2) =', type(img2))
#print('img2.shape, img2.dtype =', img2.shape, img2.dtype)
cv2.imshow('img2', img2)
while True:
    key = cv2.waitKey(30)
    if key == 27: break

# import unicodedata
# print('push key:', key)
print('push key:', chr(key))
cv2.imwrite('./image/geo_grayscale.jpg', img2)