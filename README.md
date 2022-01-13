# RobotHand
Robot Hand with Raspberry Pi 4

# Prerequisite

1. Necessary equipment :
    - Raspberry Pi 4 model B 4GB
    - Raspberry Pi Camera
    - Adafruit 16-Channel (pca9685)
    - Servo Motor x5
    - Dupont female female x4
    - Dupont mal mal x2
    - Female DC Power adapter - 2.1mm
    - 5V alimentation
    - 3D printer
    - Elastic
    - Fishing line
    - Glue 


2. Install Python packages (on Raspberry pi 4): 
    - mediapipe-rpi4 
  `sudo pip3 install mediapipe-rpi4`
    - opencv-python
  `sudo apt-get install python3-opencv`
    - Adafruit servokit
  `sudo pip3 install adafruit-circuitpython-servokit`


3. Configuring your Pi for I2C
  Before you can get started with I2C on the Pi, you'll need to run through a couple quick steps
    https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

# The cabling
  ![Connection](https://user-images.githubusercontent.com/78727838/139223432-ae8f7b58-1f7e-485c-8543-0a986b7e3fc1.PNG)
  ### /!\ Don't try to power your servos from the RasPi's 5V power, you can easily cause a power supply brown-out and mess up your Pi! /!\
  
  
  
# 3D Model
You will find the 3D model of the hand on : https://www.thingiverse.com/thing:1691704
Created by Ryan Gross.
    

  
 
