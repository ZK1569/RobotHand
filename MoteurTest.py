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


def convert(nbr,valeurMin=200, valeurMax=360):
    
    nbr = np.interp(nbr, [valeurMin,valeurMax],[0, 180]) #----- changer les valeurs elle marchent pas la 
    
    if nbr >= 150:
        nbr = 150

    return nbr

    


def possition(doigts, valeur):
    """Quel doigt puis la possition du doigts 0 a 180"""

    valeur = convert(valeur)

    pca.servo[doigts].angle = valeur
    time.sleep(0.01)









if __name__ == '__main__':
    main()