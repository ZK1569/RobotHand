#A module that you can use every were to detect hands 
#   You must import all the lib and this code
#   After you juste need to copy and run the main fonction to make it work

import cv2
import mediapipe as mp
import time


class handDetector():
    def __init__(self, mode=False, maxhands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.machands = maxhands
        self.detectionCon = detectionCon
        self.trackCon = trackCon 

        self.mpHands = mp.solutions.hands
        #its an object
        self.hands = self.mpHands.Hands(self.mode, self.machands, self.detectionCon, self.trackCon) #Different parametre of hands :static_image_mode=False, max_num_hands=2,min_detection_confidence=0.5,min_detection_confidence=0.5)
        self.mpDraw = mp.solutions.drawing_utils#solution to put the dots on the hands 

    def findHands(self, img, draw = True ):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)#convert the img to RGB because its BGR
        self.results = self.hands.process(imgRGB)#methode who process the img and return the result 
        #print(results.multi_hand_landmarks)

        if self.results.multi_hand_landmarks:#detect if there is hands in front of the camera
            for handLms in self.results.multi_hand_landmarks:#for eatch hand 
                
                if draw: # if we wont to draw it (parameter in at the begining of the methode)
                    #mpDraw.draw_landmarks(img, handLms)#draw the dots of the hand on the original img
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)#draw the dots and the lins of the hand on the original img 
        
        return img

    def findPosition(self, img, handNo=0, draw=False): #get the position of the hands

        lmList = [] #a list with all the coordonate of hands 

        if self.results.multi_hand_landmarks: #if there is hands on the img
            myHand = self.results.multi_hand_landmarks[handNo] #detecte a specific hand


            for id, lm in enumerate(myHand.landmark):#take every point of the hand we wont 
                #print(id,lm)#brut coordonat of the dots
                h, w, c = img.shape #give the sise of the img into values 
                cx, cy = int(lm.x*w), int(lm.y*h)# the possition in x and y of the dots 
                #print (id, cx, cy)#print the possition of the points with the id 
                lmList.append([id, cx, cy]) #add the values of the hand in the list (its saved) (put all vallues in a list so its a list who wontende list)
                if draw:
                    cv2.circle(img, (cx,cy), 15, (255,0,255),cv2.FILLED)#draw a cercle on the possition if the dot n°0
                    #parameters of the circle: where to show, possition, color, idk)

        return lmList #return the list





def main():
    pTime = 0 #previous time
    cTime = 0 #courent time 

    #video object (la source le de video?)
    cap = cv2.VideoCapture(0)

    detector = handDetector()

    while True:
        success, img = cap.read() #variable

        img = detector.findHands(img) # detect hand on the img 
        lmList = detector.findPosition(img) #give the position of the hand in a list 
        if len(lmList) != 0:# if there is a hand on the img it will send the possition if no it will not send position because the ls will be null
            print(lmList[4])# show the list (if we pute an index it will just send the possition of the dot we wonted)

        cTime = time.time()
        fps = 1/(cTime-pTime) #calcule of the fps
        pTime = cTime # the previouse time becaume the corent time 

        cv2.putText(img, str(int(fps)),(10,40), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,255), 3) #to print a text on the img 
        #parameters of putText : support, the value, "taille", "le 1er ou second plan", skill, color, tikness)


        cv2.imshow("Image", img)#show the content of the camera
        cv2.waitKey(1)#idk but its not working with out it 


if __name__ == "__main__":
    main()
