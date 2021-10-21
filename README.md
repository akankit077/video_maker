# Video Maker
This application is used to generate a video from given frames

# How to run
To run the application, pass full path to the folder having all the frames required to make the video as a command line argument.<br/>
For example:
```
python3 create_video.py /home/user/folder
```

# Requirements
The following python version and modules are required for the application to work:<br/>
* Python 3
* cv2
* natsort
* sys
* os

# Assumptions
* All the frames are having same width and height
* All the frames are in same format i.e., either ".jpg", ".jpeg" or ".png"
* No frames are missing