# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 13:38:53 2019

@author: Ten7
"""

import os
import cv2
import numpy as np
import imutils
from skimage import feature
from scipy.spatial import ConvexHull
import os
import dlib
import skimage

    
def cropface():
    path_img = cv2.imread("a.jpg")

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    
    gray = cv2.cvtColor(path_img, cv2.COLOR_BGR2GRAY)
    
    faces= detector (path_img)[0]
    
#    for face in faces:
#        x1 = face.left()
#        y1 = face.top()
#        x2 = face.right()
#        y2 = face.bottom()
        
    sp=predictor(gray,faces)
    
    landmarks = predictor(path_img, faces)
    
    x = landmarks.part(21).x
    y = landmarks.part(30).y
    xa = landmarks.part(22).x
    ya = landmarks.part(30).y
    xb = landmarks.part(21).x
    yb = landmarks.part(27).y
    xc = landmarks.part(22).x
    yc = landmarks.part(27).y
    
    titik=[[x,y], [xa,ya], [xb,yb], [xc,yc]]
    
#    cv2.circle(path_img, (x, y), 4, (255, 0, 0), -1)
#    cv2.circle(path_img, (xa, ya), 4, (255, 0, 0), -1)
#    cv2.circle(path_img, (xb, yb), 4, (255, 0, 0), -1)
#    cv2.circle(path_img, (xc, yc), 4, (255, 0, 0), -1)
        
#    landmarks = np.array([[p.x,p.y] for p in sp.parts()])
    
    
#    vertices = ConvexHull(poin).vertices
    Y, X = skimage.draw.rectangle((xb,yb), (xa,ya))
    cropped_img = np.zeros(gray.shape, dtype=np.uint8)
    cropped_img[Y,X] = gray[Y,X]
##    cropped = gray[yb:ya, xb:xa]
#    rect = cv2.boundingRect(cropped_img)
#    x,y,w,h = rect
#    result = cropped_img[y:y+h, x:x+w].copy()
##    print(min(result))
    return result
    
    
def main():
    img = cropface()
    cv2.imshow('image',img)
#    cv2.imwrite('test_write.jpg',img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__=='__main__':
        main()