# Facial-Recognition
This GitHub includes the necessary files to run the major aspects of the application including the encodin file and the 
facial recognition xml
to use this copy these files into a python project and download the necessary dependencies which includes

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


as well as a c interpreter in visual studios

once the dependencies are collected (i used pycharm on windows) you should create a 'dataset' directory in the project directory
this is where all the pictures will be stored to encode
after that you nned to create your own twilio account and adjust the information to send from your twilio numer, to your own number
and use your account sid and token as i would rather not pay for a real account at this point in time.

once all the necessary directories are there and all the twilio is correct and the dependencies are created you can use this code. 
to run begin by adding to the dataset you can either run the Add_encode.py which will use your computer camera to take and store pictures 
of your face in the dataset under the chosen name. Alternatively you can take pictures from your local machine or anywhere else and store 
them in the dataset by creating a new name directory and saving the pictures in there. If you store pictures not by using Add_encode.py 
make sure you run encode_faces.py before you try to run any facial recognition on video software.  Once your dataset is filled and the
faces are encoded you are ready to run video recognition.  

Running recognize_faces_video.py has several options. If you run the code as is it will bring up a video that shows what the camera is 
picking up and the faces as well as the name of the person. However if you run it from a terminal you can change certain arguments you
can make the video feed not show up or increase accuracy at the cost of more processing power required check the arg parser for options.
For recognize_faces_video_file.py it requires that you give it a path to a video file which means read the arg parser are determine what
is needed for that, it has similar abilities to the video feed file.

"it works on my machine" which is many programmers downfall but i havent tested this on other computers as i only have 1 with a camera
so if you have any questions email me at hilla4@duq.edu. In the future given time i intend to add other functionality to the program 
when it detects unknown faces as well as a ui for easier use.
