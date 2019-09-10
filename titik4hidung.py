import cv2
import numpy as np
import dlib


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

def titik():
    path_img = cv2.imread("a.jpg")
    
    path_img = cv2.cvtColor(path_img, cv2.COLOR_BGR2GRAY)

    faces = detector(path_img)
    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        #cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        landmarks = predictor(path_img, face)

#        for n in range(0, 68):
        x = landmarks.part(21).x
        y = landmarks.part(30).y
        xa = landmarks.part(22).x
        ya = landmarks.part(30).y
        xb = landmarks.part(21).x
        yb = landmarks.part(27).y
        xc = landmarks.part(22).x
        yc = landmarks.part(27).y
        
        cv2.circle(path_img, (x, y), 4, (255, 0, 0), -1)
        cv2.circle(path_img, (xa, ya), 4, (255, 0, 0), -1)
        cv2.circle(path_img, (xb, yb), 4, (255, 0, 0), -1)
        cv2.circle(path_img, (xc, yc), 4, (255, 0, 0), -1)
        
        cv2.imshow("Frame", path_img)
        cv2.imwrite('test_write.jpg',path_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    img = titik()
    

if __name__=='__main__':
        main()
    