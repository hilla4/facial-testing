# Facial-Recognition
To be able to run this code you need to clone this onto the python path then download visual studios with a c compiler
as some of the dependencies will not be installable without it. Following that you can download all the following
 dependencies.

Click	7.0	7.0

Pillow	6.2.1	6.2.1

PyJWT	1.7.1	1.7.1

PySide2	5.13.2	5.13.2

asgiref	3.2.3	3.2.3

certifi	2019.11.28	2019.11.28

chardet	3.0.4	3.0.4

cmake	3.15.3	3.15.3

dlib	19.18.0	19.18.0

face-recognition	1.2.3	

face-recognition-models	0.3.0	

idna	2.8	2.8

imutils	0.5.3	0.5.3

numpy	1.17.4	1.17.4

opencv-python	4.1.1.26	4.1.2.30

pip	19.3.1	19.3.1

pytz	2019.3	2019.3

requests	2.22.0	2.22.0

setuptools	41.2.0	42.0.2

shiboken2	5.13.2	5.13.2

six	1.13.0	1.13.0

sqlparse	0.3.0	0.3.0

twilio	6.34.0	6.34.0

urllib3	1.25.7	1.25.7


   Once all the necessary dependencies are there you can use this code. To run this code you run the mainWindow.py file
which will open the UI which has a few options. In the top right there is a button labeled "..." which clicking will allow 
you to set your name, your phone number that will receive the texts and your email clicking ok will store it into the 
database. Once you are in the database you can click the "Add to Dataset" button. This button gives you the option to 
add pictures to the dataset that will be recognized when running the video analysis. You can add pictures by either 
taking pictures with your camera or browsing your computer for saved pictures, once added the database will need to 
re encode the dataset  so the larger the dataset gets the longer this will take. Once you have added pictures to the
dataset you can run either analysis on live video or on a video file which will analyze the video and if an 
unrecognized user is in the feed for 20 frames it will send a text to the phone number in the database alerting you 
that there is an unauthorized user and it will save a picture to the directory that has the project.
 
   Known issues:
   
This application is currently unable to send texts to any numbers that are not mine because the application im using to 
send texts is a free trial, with a paid subscription this would be solved.

If you try to add to the dataset without specifying a name it will fail.

Running any video analysis without having a camera