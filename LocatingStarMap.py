#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:05:28 2020

@author: furkan
"""
import cv2

method = cv2.TM_SQDIFF_NORMED

small_area = cv2.imread("Small_area.png")
star_map  = cv2.imread("StarMap.png")


result = cv2.matchTemplate(small_area, star_map, method)

# We want the minimum squared difference
mn,_,mnLoc,_ = cv2.minMaxLoc(result)

# Draw the rectangle
# Extract the coordinates of our best match
MPx,MPy = mnLoc

# Template Size
trows,tcols = small_area.shape[:2]

# Draw the rectangle on StarMap
cv2.rectangle(star_map, (MPx,MPy),(MPx+tcols,MPy+trows),(0,0,255),2)

cv2.imshow('output',star_map)
print(MPx,MPy)
cv2.waitKey(1)
