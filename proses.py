import cv2
import numpy as np
import skimage
from imutils import paths
import dlib
from PIL import Image, ImageTk
import Latihan as lat
from scipy.spatial import ConvexHull
from sklearn.neural_network import MLPClassifier as ann
import os


class ImageProses():

    def __init__(self, foldertrain):
        self.foldertrain = foldertrain
        
# membaca gambar dari path get
    def getImgTrain(self):    
        pathImgTrain=[]
        for path in paths.list_images(self.foldertrain):
            pathImgTrain.append(path)
        return pathImgTrain
    
# meload gambar setelah pembacaan get            
    def loadImgTrain(self):
        pathImgTrain = self.getImgTrain()
        imgTrain = []
        for image in pathImgTrain:
            img = cv2.imread(image)
            imgTrain.append(img)
        return imgTrain
    
#prapengolahan Gray dan EQHist        
    def prapengolahan(self, image):
        gbrGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gbrHist = cv2.equalizeHist(gbrGray)
        
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
                
        faces= detector (image)[0]
        sp=predictor(gbrGray,faces)
        landmarks = np.array([[p.x,p.y] for p in sp.parts()])
        vertices = ConvexHull(landmarks). vertices
        Y, X = skimage.draw.polygon(landmarks[vertices, 1], landmarks[vertices, 0])
        cropped_img = np.zeros(gbrGray.shape, dtype=np.uint8)
        cropped_img[Y,X] = gbrGray[Y,X]
        rect = cv2.boundingRect(cropped_img)
        x,y,w,h = rect
        hasilCrop = cropped_img[y:y+h, x:x+w].copy()
        
        return hasilCrop, gbrGray, gbrHist     

    
    def skintrain(self, imgTrain):
        
        lower = np.array([0, 48, 80], dtype = "uint8")
        upper = np.array([20, 255, 255], dtype = "uint8")
        
        # Convert BGR to HSV and parse HSV

        converted = cv2.cvtColor(imgTrain, cv2.COLOR_BGR2HSV)
        skinMask = cv2.inRange(converted, lower, upper)
        
        # using an elliptical kernel
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (11, 11))
        skinMask = cv2.erode(skinMask, kernel, iterations = 2)
        skinMask = cv2.dilate(skinMask, kernel, iterations = 2)
        # 
        #	# blur the mask to help remove noise, then apply the
        #	# mask to the frame
        skinMask = cv2.GaussianBlur(skinMask, (3, 3), 0)
        skin = cv2.bitwise_and(imgTrain, imgTrain, mask = skinMask)
        hasil = cv2.cvtColor(skin, cv2.COLOR_BGR2RGB)
    
        return hasil, skinMask, skin
    
    def loadGambarPraTrain(self, hasilPrap):
        pathHasilPra = hasilPrap
        citraTrain = []
        for image in pathHasilPra :
            im = np.float32(image)/255.0
            citraTrain.append(im)
        return citraTrain      
           
    def buildLabel(self):
        label = []
        path = self.getImgTrain()            
        for itemimg in path:
            label.append(os.path.split(os.path.dirname(itemimg))[-1])
        return label
    
    def buildTrainData(self):
        imgTrain = []
        imageLoad = self.loadImgTrain()
        
        for citra in imageLoad:
            hasilCrop, gbrGray, gbrHist = self.prapengolahan(citra)             
            nonZeroCrop = cv2.countNonZero(hasilCrop)

            hasilSkin, maskSkin, warnaSkin  = self.skintrain(citra)
            nonZeroSkin = cv2.countNonZero(maskSkin)
                        
            persenFace = nonZeroCrop / nonZeroSkin  
            persenNonFace = (nonZeroSkin - nonZeroCrop) / nonZeroSkin
            
            imgTrain.append([persenNonFace, persenFace])      
        return imgTrain
    
    def buildTestData(self,textboxdatatesting):
        imgTest = []
        gambar = self.loadImgTest(textboxdatatesting)
        
        hasilCrop, gbrGray, gbrHist = self.prapengolahan(gambar)
        hasilSkin, maskSkin, warnaSkin  = self.skintrain(gambar)
        
        nonZeroCrop = cv2.countNonZero(hasilCrop)
        nonZeroSkin = cv2.countNonZero(maskSkin)
        
        persenFace = nonZeroCrop / nonZeroSkin  
        persenNonFace = (nonZeroSkin - nonZeroCrop) / nonZeroSkin
        
        imgTest.append([persenNonFace, persenFace])
        return imgTest, gbrHist, hasilSkin, persenNonFace

    def ann(self, fiturtraning, fiturtesting, label):                        
        klasifikasi = ann(hidden_layer_sizes=200, activation="relu", max_iter=1000)
        klasifikasi.fit(fiturtraning, label)
        klasifikasihasil = klasifikasi.predict(fiturtesting)

        return klasifikasihasil, fiturtesting
         
            
#==============================================================================
                            # BLOK TESTING
#==============================================================================
    
# meload gambar testing
    def loadImgTest(self,pathFolderTest):
        img = cv2.imread(pathFolderTest)
        return img
           
    def pilihhue(self,pathFolderTest):
        gbrhue = cv2.imread(pathFolderTest)
        hsv_img = cv2.cvtColor(gbrhue, cv2.COLOR_BGR2HSV)
        h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
        cv2.imshow("Hue",h)
        return h
    
    def pilihstr(self,pathFolderTest):
        gbrstr = cv2.imread(pathFolderTest)
        hsv_img = cv2.cvtColor(gbrstr, cv2.COLOR_BGR2HSV)
        h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
        cv2.imshow("Saturation",s)
        return s
    
    def pilihvle(self,pathFolderTest):
        gbrvle = cv2.imread(pathFolderTest)
        hsv_img = cv2.cvtColor(gbrvle, cv2.COLOR_BGR2HSV)
        h, s, v = hsv_img[:, :, 0], hsv_img[:, :, 1], hsv_img[:, :, 2]
        cv2.imshow("Value",v)
        return v
    
    def pilihhsv(self,pathFolderTest):
        gbrhsv = cv2.imread(pathFolderTest)
        hsvimg = cv2.cvtColor(gbrhsv, cv2.COLOR_BGR2HSV)
        out = cv2.cvtColor(hsvimg, cv2.COLOR_BGR2RGB)        
        cv2.imshow("hsv",out)
        return hsvimg
