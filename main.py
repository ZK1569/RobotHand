import cv2
import time
import numpy as np
import mediapipe as mp
import Hand_module as htm
import math

#############################
wCam, hCam = 1280,720  #save the values of the camera 
#############################

cap = cv2.VideoCapture(0) #importing the camera 
cap.set(3,wCam) #Forcing the values of the camera 
cap.set(4,hCam)

pTime = 0 #time set 0

detector = htm.handDetector(detectionCon=0.5)

#Possition de basse des doigts
thumbPos = 100
indexPos = 100
middle = 100
ring = 100
pinky = 100

while True:
    seccess, img = cap.read()

    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        #print (lmList[4],lmList[8]) # Possition brut des doigts

        #Tacking the values vrome the list and put it in variables 
        thumbFingerX, thumbFingerY = lmList[4][1], lmList[4][2]     #Thumb finger     
        indexFingerX, indexFingerY = lmList[8][1], lmList[8][2]     #Index finger  
        middleFingerX, middleFingerY = lmList[12][1], lmList[12][2] #Middle finger
        ringFingerX, ringFingerY = lmList[16][1], lmList[16][2]     #Ring finger 
        pinkyFingerX, pinkyFingerY = lmList[20][1], lmList[20][2]   #Pinky Finger 
        wristX, wristY = lmList[0][1], lmList[0][2]                 #wrist of the model
        
        #cx, cy = (x1+x2)//2, (y1+y2)//2 #center between the point 4 and 8 ---- je sais pas si utile 

        #cv2.circle(img, (x1,y1), 15,(255,255,0), cv2.FILLED) ------ dessin des cercle 
        #cv2.circle(img, (x2,y2), 15,(255,255,0), cv2.FILLED)

        #Draw the lines between the finger and the wrist
        cv2.line(img,(wristX,wristY),(thumbFingerX,thumbFingerY), (255,255,0),2) 
        cv2.line(img,(wristX,wristY),(indexFingerX,indexFingerY), (255,255,0),2)
        cv2.line(img,(wristX,wristY),(middleFingerX,middleFingerY), (255,255,0),2)
        cv2.line(img,(wristX,wristY),(ringFingerX,ringFingerY), (255,255,0),2)
        cv2.line(img,(wristX,wristY),(pinkyFingerX,pinkyFingerY), (255,255,0),2)
        
        #Calcule the distance between the 2 points 
        thumb = math.hypot(wristX-wristY, thumbFingerX-thumbFingerY)
        index = math.hypot(wristX-wristY, indexFingerX-indexFingerY)
        middle = math.hypot(wristX-wristY, middleFingerX-middleFingerY)
        ring = math.hypot(wristX-wristY, ringFingerX-ringFingerY)
        pinky = math.hypot(wristX-wristY, pinkyFingerX-pinkyFingerY)

        #print ("Thumb = ", thumb)
        #print ("Index = ", index)
        #print ("Middle = ", middle)
        #print ("Ring = ", ring)
        #print ("Pinky = ", pinky, "\n")

        #convert the lenght to 0 at 100
        thumbF = np.interp(thumb, [200,360],[0, 100]) #----- changer les valeurs elle marchent pas la 
        indexF = np.interp(index, [155,360],[0, 100])
        middleF = np.interp(middle, [130,250],[0, 100]) # -------- c'est toujours pas bon cette merde 
        ringF = np.interp(ring, [100,260],[0, 100])
        pinkyF = np.interp(pinky, [100,200],[0, 100])

        #print ("Thumb = ", thumb)
        #print ("Index = ", index)
        #print ("Middle = ", middle)
        #print ("Ring = ", ring)
        #print ("Pinky = ", pinky, "\n")

        """
        Code special Raspberry:
            - Les fonctions a envoyer pour les moteurs
            - Ajouter au prealable les classes des moteurs
            - Tester avant avec le Raspberry et les moteurs hors de ce code

        """

        




        #print (length)

        #hand range 50 - 300
        #volume range -60 - 0


        #volBar = np.interp(length, [50,300],[400, 150]) #produit en croix 

        #if length < 50:
        #    cv2.circle(img, (cx,cy), 7,(0,255,0), cv2.FILLED)


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime


    cv2.putText(img, str(int(fps)),(15,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,0), 2)
    cv2.imshow("Camera", img)
    cv2.waitKey(1)
#End 