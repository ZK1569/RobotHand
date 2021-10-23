# RobotHand
Robot Hand with Raspberry Pi 4

# Prerequisite
1. To be able to use this, you must first install with thise libraries on your pc :
  - mediapipe (supported by Python 3.6 to 3.8) ```pip install mediapipe```
  - opencv-python ```pip install opencv-python```

2. To be able to use this on a Raspberry Pi4 install : 
  - mediapipe-rpi4 
```pip3 install mediapipe-rpi4``` 
  - opencv-python
```pip3 install opencv-python```
  - (le truque pour controller les servo-moteur)
```meme commende mais je sais pas```

3. If you can't install opencv-python on your PC or Raspberry, try: 
  - ```pip3 install --upgrade pip```
  - ```pip3 install --upgrade numpy```

```
$ sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng12-dev 
$ sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev 
$ sudo apt-get install libxvidcore-dev libx264-dev 
$ sudo apt-get install qt4-dev-tools libatlas-base-dev ```
