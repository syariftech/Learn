import cv2
import numpy as np
from imutils import paths
from skimage import feature
from PIL import Image, ImageTk
import Latihan as lat
from skimage import feature
from scipy.spatial import ConvexHull

#from sklearn.neural_network import MLPClassifier as ann
#import os


class ImageProses():

    def __init__(self):
        self.pixel = ''
        self.persent = ''
# membaca gambar dari path get
    def getImgTrain(self, pathFolderTrain):    
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
    
#prapengolahan Gray dan EQHist        
    def prapengolahan(self, image):
        gbrGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gbrHist = cv2.equalizeHist(gbrGray)   
        return gbrHist
            
    def cropface(self, hasilpraolah):
        
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
        gray = cv2.cvtColor(images, cv2.COLOR_BGR2GRAY)   
   
        faces= detector (path_img)[0]
        sp=predictor(gray,faces)
        landmarks = np.array([[p.x,p.y] for p in sp.parts()])
        vertices = ConvexHull(landmarks). vertices
        Y, X = skimage.draw.polygon(landmarks[vertices, 1], landmarks[vertices, 0])
        cropped_img = np.zeros(gray.shape, dtype=np.uint8)
        cropped_img[Y,X] = gray[Y,X]
        rect = cv2.boundingRect(cropped_img)
        x,y,w,h = rect
        result = cropped_img[y:y+h, x:x+w].copy()
                
        return result
    
    def skintrain(self, hasilpraolah):        
                
        lower = np.array([0, 48, 80], dtype = "uint8")
        upper = np.array([20, 255, 255], dtype = "uint8")
        
        # Convert BGR to HSV and parse HSV
#        frame = imutils.resize(img, width = 400)
        converted = cv2.cvtColor(hasilpraolah, cv2.COLOR_BGR2HSV)
        skinMask = cv2.inRange(converted, lower, upper)
        
        # using an elliptical kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        skinMask = cv2.erode(skinMask, kernel, iterations = 2)
        skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
        # 
        #	# blur the mask to help remove noise, then apply the
        #	# mask to the frame
        skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
        skin = cv2.bitwise_and(hasilpraolah, hasilpraolah, mask = skinMask)
        hasil = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)
        
                
#        cv2.imshow("images", np.hstack([frame, skin]))
        return hasil
        
        
    def getLabelTrain(self):
        label = []
        path = pathImgTrain()            
        for itemimg in path:
            label.append(os.path.split(os.path.split.dirname(itemimg))[-1])
        return label
    
    def buildTrainData(self):
        imgTrain = []
        path = self.getImgTrain()
        images = self.loadImgTrain(path)
        img = []
        for image in images:
            img.append(image)
        i = 0
        for gambar in img:
            hasilpraolah = self.prapengolahan(gambar)
            hasilskin = self.skintrain(hasilpraolah)        
            hasilcrop = self.cropface(hasilpraolah)
            nonzeroskin = cv2.countNonZero(hasilskin)
            nonzerocrop = cv2.countNonZero(hasilcrop)
            imgTrain.append([nonzeroskin, nonzerocrop])      
        return imgTrain
    
    
    def loadImgPraTrain(self, hasil_pra):
        pathHasil_pra = hasil_pra
        imgTrain = []
        for image in pathHasil_pra:
            im = np.float32(image)/255.0
            imgTrain.append(im)
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
#        cv2.imshow("Histogram",gbrHist)
        return gbrHist
    
    def pilihhue(self,pathFolderTest):
        gbrhue = cv2.imread(pathFolderTest)
        hsv_img = cv2.cvtColor(gbrhue, cv2.COLOR_BGR2HSV)
        h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
#        cv2.imshow("Hue",h)
        return h
    
    def pilihstr(self,pathFolderTest):
        gbrstr = cv2.imread(pathFolderTest)
        hsv_img = cv2.cvtColor(gbrstr, cv2.COLOR_BGR2HSV)
        h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
#        cv2.imshow("Saturation",s)
        return s
    
    def pilihvle(self,pathFolderTest):
        gbrvle = cv2.imread(pathFolderTest)
        hsv_img = cv2.cvtColor(gbrvle, cv2.COLOR_BGR2HSV)
        h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
#        cv2.imshow("Value",v)
        return v
    
    def pilihhsv(self,pathFolderTest):
        gbrhsv = cv2.imread(pathFolderTest)
        hsvimg = cv2.cvtColor(gbrhsv, cv2.COLOR_BGR2HSV)
        out = cv2.cvtColor(hsvimg, cv2.COLOR_BGR2RGB)        
#        cv2.imshow("hsv",out)
        return hsvimg
        
    def skintesting(self,pathFolderTest):
                
        img = cv2.imread(pathFolderTest)

        a = img.shape[0]
        b = img.shape[1]
        
        c = (a*b)
        self.setpixel(c)
        print(self.pixel)
        
        lower = np.array([0, 48, 80], dtype = "uint8")
        upper = np.array([20, 255, 255], dtype = "uint8")
        
        converted = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        skinMask = cv2.inRange(converted, lower, upper)
        
        # using an elliptical kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        skinMask = cv2.erode(skinMask, kernel, iterations = 2)
        skinMask = cv2.dilate(skinMask, kernel, iterations = 2)

        # blur the mask to help remove noise, then apply the
        # mask to the frame
        skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
        skin = cv2.bitwise_and(img, img, mask = skinMask)
        
        # deteksi skin tampil
#        cv2.imshow("images", np.hstack([skin]))
        hasil = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)
        
        print (cv2.countNonZero(skinMask))
        self.setpersent(cv2.countNonZero(skinMask), c)
        
        return hasil
        
    def setpixel(self, pixel):
        self.pixel = pixel
        
    def gepixel(self):
        return self.pixel
    
    def setpersent(self, skin, pixel):
        self.persent = (skin / pixel) * 100
    
        
    def getpersent(self):
        return round(self.persent)
