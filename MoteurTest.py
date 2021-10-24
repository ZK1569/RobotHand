import time    
from adafruit_servokit import ServoKit    

#Constants
nbPCAServo=16 

#Parameters
MIN_IMP  =[500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500, 500]
MAX_IMP  =[2700, 2700, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500, 2500]
MIN_ANG  =[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
MAX_ANG  =[180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180, 180]

#Objects
pca = ServoKit(channels=16)


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


def convert(nbr):
    """Convert le lenght de la camera
    en valeur pouvent etre utiiser par les moteur 
    donc entre 0 à 180 (je pense)"""
    


def possition(doigts, valeur):
    convert(valeur)
    """Change la possition des moteurs
    pas de boucle elle sera pas l'appelle de fonction
    """









if __name__ == '__main__':
    init()
    main()