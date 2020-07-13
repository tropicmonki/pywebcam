#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 13:29:59 2020

access python webcam to test

@author: tj_
"""
import cv2

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break

vc.release() #prevent webcam locking
cv2.destroyWindow("preview")
