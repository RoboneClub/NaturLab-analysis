#Importing the Libraries
import cv2
from matplotlib import image
import numpy as np
from fastiecm import fastiecm

#Variable with the image number
i = 154

original = cv2.imread('image_'+str(i)+'.jpg')

def contrast_stretch(im):

    in_min = np.percentile(im, 5)
    in_max = np.percentile(im, 95)
  
    out_min = 0.0
    out_max = 255.0
 
    out = im - in_min
    out *= ((out_min - out_max) / (in_min - in_max))
    out += in_min

    return out

#A function to calculate the ndvi in the image
def calc_ndvi(image):

    b, g, r = cv2.split(image)

    bottom = (r.astype(float) + b.astype(float))

    bottom[bottom==0] = 0.01

    ndvi = (r.astype(float) - b.astype(float)) / bottom

    print(ndvi[ndvi < 0.9].max())

    return ndvi
    
  
def show():

    contrasted = contrast_stretch(original)
    
    ndvi = calc_ndvi(contrasted)

    ndvi_contrasted = contrast_stretch(ndvi)

    color_mapped_prep = ndvi_contrasted.astype(np.uint8)

    color_mapped_image = cv2.applyColorMap(color_mapped_prep, fastiecm)

    cv2.imwrite('color_mapped_image_'+str(i)+'.png', color_mapped_image)


show()





