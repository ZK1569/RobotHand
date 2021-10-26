import time    
import numpy as np
from adafruit_servokit import ServoKit    

#Constants
nbPCAServo=16 

#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2700, 2700, 2700, 2700, 2700, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

#Objects
pca = ServoKit(channels=16)

#initialisation
for i in range(nbPCAServo):
    pca.servo[i].set_pulse_width_range(MIN_IMP[i] , MAX_IMP[i])

# function main 
def main():

    action()


def action():
    for i in range(nbPCAServo):
        for j in range(MIN_ANG[i],MAX_ANG[i],1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        for j in range(MAX_ANG[i],MIN_ANG[i],-1):
            print("Send angle {} to Servo {}".format(j,i))
            pca.servo[i].angle = j
            time.sleep(0.01)
        pca.servo[i].angle=None #disable channel
        time.sleep(0.5)


def verification(var):
    verif = False
    if type(var) == list:
        if len(var) == 5:
            for i in var:
                if i == 0 or i == 1:
                    verif = True 
    
    return verif 
                
def positionMoteur(fingers):
    
    if verification(fingers):
        for nbrMotor in range(0,5):
            pca.continuous_servo[nbrMotor].throttle = fingers[nbrMotor]
            time.sleep(0.01)





if __name__ == '__main__':
    main()