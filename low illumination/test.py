import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)
time.sleep(3)
background=[]
for i in range(50):
    ret,bg = cap.read()
    if ret is True and i>25:
    	bg = np.flip(bg,axis=1)
    	bg_hsv = cv2.cvtColor(bg, cv2.COLOR_BGR2HSV)
    	background.append(bg_hsv)



print("""
         Background recordered .....................
    """)
while(cap.isOpened()):
    ret, img = cap.read()

    # Flipping the image (Can be uncommented if needed)
    img = np.flip(img,axis=1)

    # Converting image to HSV color space.
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    brightness = hsv[:,2].mean()
    if brightness<70:
    	idx = np.random.randint(0,len(background))
    	bg_hsv = background[idx]
    	hsv[:,2] = bg_hsv[:,2]
    	img = cv2.cvtColor(bg_hsv, cv2.COLOR_HSV2BGR)

    cv2.imshow('Display',img)
    k = cv2.waitKey(10)
    if k == 27:
        break
