#Importing libraries
from patchify import patchify
import cv2

#Reading the image that is going to be patched
img = cv2.imread("image_.jpg")

#Resizing the img to 4000 x 3000 
img = cv2.resize(img, (4000, 3000))

#Patchifying the image
patches_img = patchify(img, (1000,1000,3), step=500)
for i in range(patches_img.shape[0]):
    for j in range(patches_img.shape[1]):
        single_patch_img = patches_img[i, j, 0, :, :, :]
        if not cv2.imwrite('patches/' + 'image_' + '_'+ str(i)+str(j)+'.jpg', single_patch_img):
            raise Exception("Could not write the image")