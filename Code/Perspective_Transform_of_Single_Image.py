# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 20:08:20 2021

@author: Sonu
"""

import numpy as np
import cv2

area_of_interest = []
area_of_projection = []

#Creating a mouse call back function to store the corrdinates of the image points clicked.
def click_event(event, x, y, flags, params): 
    # If event is Left Button Click then store the coordinate in the area_of_interest lists
    if event == cv2.EVENT_LBUTTONUP:
        cv2.circle(img,(x,y),2,(255,0,0),-1)
        area_of_interest.append([x,y])
        print(x, ' ', y)
        # displaying the coordinates on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img, str(x) + ',' +str(y), (x,y), font, 1, (255, 0, 0), 2) 
        cv2.imshow('image', img)
        
    # If event is Right Button Click then store the coordinate in the area_of_projection lists
    if event == cv2.EVENT_RBUTTONUP:
        cv2.circle(img_copy,(x,y),2,(255,0,0),-1)
        area_of_projection.append([x,y])
        print(x, ' ', y) 
        # displaying the coordinates on the image window 
        font = cv2.FONT_HERSHEY_SIMPLEX 
        cv2.putText(img_copy, str(x) + ',' +str(y), (x,y), font, 1, (255, 0, 0), 2) 
        cv2.imshow('new_image', img_copy)        
  
# reading the image 
img = cv2.imread('homography_source_desired_images1.jpg', 1) 

# creating copy of the image
img_copy = img.copy()
final_copy = img.copy()
#Naming the Window
cv2.namedWindow('image')
# displaying the image 
cv2.imshow('image', img) 
# setting mouse hadler for the image and calling the click_event() function
cv2.setMouseCallback('image', click_event) 
# wait for a key to be pressed to exit 
cv2.waitKey(0) 
# close the window 
cv2.destroyAllWindows()

cv2.namedWindow('new_image')
cv2.imshow('new_image', img_copy) 
cv2.setMouseCallback('new_image', click_event) 
cv2.waitKey(0)  
cv2.destroyAllWindows()

print('Coordinates of area of interest', area_of_interest)
print('Coordinates of area of projection', area_of_projection)

height, width = final_copy.shape[:2]
area_of_interest = np.float32(area_of_interest)
area_of_projection = np.float32(area_of_projection)

#Obtaining a Perspective transform between the two set of image points
M = cv2.getPerspectiveTransform(area_of_interest, area_of_projection)
dst = cv2.warpPerspective(final_copy, M, (width,height))

cv2.imshow('warped image', dst) 
cv2.waitKey(0) 
cv2.destroyAllWindows()
