import cv2
import time
import Hand_module as htm
import MoteurTest as mt


#############################
wCam, hCam = 1280,720  #save the values of the camera 
#############################

cap = cv2.VideoCapture(0) #importing the camera 
cap.set(3,wCam) #Forcing the values of the camera 
cap.set(4,hCam)

pTime = 0 #time set 0

detector = htm.handDetector(detectionCon=0.75)

#list of fingers I nead
tipIds = [4, 8, 12, 16, 20]


while True:
    seccess, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        fingers = []

        #thumb
        if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)
        
        #other fingers
        for i in range(1,5):
            if lmList[tipIds[i]][2] < lmList[tipIds[i]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        mt.positionMoteur(fingers) #action send to the motor fonction

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    cv2.putText(img, str(int(fps)),(15,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0), 2)
    cv2.imshow("Camera", img)
    cv2.waitKey(1)
#End 
