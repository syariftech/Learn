import cv2
import numpy as np
from imutils import paths
from skimage import feature
from PIL import Image, ImageTk
import Latihan as lat
#from sklearn.neural_network import MLPClassifier as ann
#import os


class ImageProses():

    def prapengolahan(self, pathFolderTrain):
        
# membaca gambar dari path get
        pathImgTrain=[]
        for path in paths.list_images(pathFolderTrain):
            pathImgTrain.append(path)
        return pathImgTrain
    
# meload gambar setelah pembacaan get            
    def loadImgTrain(self,pathFolderTrain):
        pathImgTrain = pathFolderTrain
        imgTrain = []
        for image in pathImgTrain:
            img = cv2.imread(image)
            imgTrain.append(img)
        return imgTrain
    
#==============================================================================
                            # BLOK TESTING
#==============================================================================
    
# meload gambar testing
    def loadImgTest(self,pathFolderTest):
        img = cv2.imread(pathFolderTest)
#        cv2.imshow("ori",img)
        return img
    
# meload gambar pengolahan Histogram
        
    def ImgHeist(self,pathFolderTest):
        img = cv2.imread(pathFolderTest)
#        cv2.imshow("h",img)
        imghist = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gbrHist = cv2.equalizeHist(imghist)
        return gbrHist
    
    def pilihhue(self,pathFolderTest):
        gbrhue = cv2.imread(pathFolderTest)
        hsv_img = cv2.cvtColor(gbrhue, cv2.COLOR_BGR2HSV)
        h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
        cv2.imshow("h",h)
        return gbrhue
    
    def pilihstr(self,pathFolderTest):
        gbrstr = cv2.imread(pathFolderTest)
        hsv_img = cv2.cvtColor(gbrstr, cv2.COLOR_BGR2HSV)
        h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
        cv2.imshow("Saturation",s)
        return gbrhstr
        
    
    