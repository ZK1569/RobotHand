import cv2
import time
import Hand_module as htm
import Motor as mt

#importing the camera
cap = cv2.VideoCapture(0)  

#Camera settings
wCam, hCam = 1280,720
#Parameter of camera applied 
cap.set(3,wCam)
cap.set(4,hCam)

detector = htm.handDetector(detectionCon=0.75)

#List of fingers neaded
tipIds = [4, 8, 12, 16, 20]

pTime = 0
while True:
    seccess, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img)
    
    #I hand detecred 
    if len(lmList) != 0:
        fingers = []

        #thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(0)
        else:
            fingers.append(1)
        
        #other fingers
        for i in range(1,5):
            if lmList[tipIds[i]][2] < lmList[tipIds[i]-2][2]:
                fingers.append(0)
            else:
                fingers.append(1)  
        #Motor mouvement
        mt.positionMoteur(fingers) 

    #FPS calculator 
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    #Show camera
    cv2.putText(img, str(int(fps)),(15,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0), 2)
    cv2.imshow("Camera", img)
    cv2.waitKey(1)
