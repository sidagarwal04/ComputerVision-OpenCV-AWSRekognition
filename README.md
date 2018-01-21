# ComputerVision-OpenCV-AWSRekognition

# Overview
Here is the code for image recognition using OpenCV and AWS Rekognition service with input from webcam. OpenCV tracks faces and monitors for smiles, when a smile is detected a picture is saved locally on the computer, sent the image to AWS S3 bucket, then AWS Rekognition Service is invoked to analyze that picture, and the results are sent back to console. We need a webcam to provide video input to the program.  

# Dependencies
- Install Ubuntu 16.04, https://www.ubuntu.com/download/desktop
- Install Python 2.7.14, https://www.python.org/downloads/
- Install OpenCV2 with python bindings, http://docs.opencv.org/2.4/doc/tutorials/introduction/linux_install/linux_install.html
- Boto3 package, `$ pip install boto3`, https://github.com/boto/boto3
- Create a AWS S3 Bucket, http://docs.aws.amazon.com/AmazonS3/latest/gsg/SigningUpforS3.html (Note: The bucket needs open write premissions. Make sure to add the bucket name in the python script)
- Authenticating to AWS Servers, `$ aws configure`, https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html
- haarcascade_frontalface_default.xml, https://github.com/sidagarwal04/ComputerVision-OpenCV-AWSRekognition/blob/master/haarcascade_frontalface_default.xml
- haarcascade_smile.xml, https://github.com/sidagarwal04/ComputerVision-OpenCV-AWSRekognition/blob/master/haarcascade_smile.xml

# Note: 
Ubuntu 16.04 actually ships out-of-the-box with both Python 2.7 and Python 3.5 installed. The actual versions are:
 1. Python 2.7.12 (used by default when you type python in your terminal).
 2. Python 3.5.2 (can be accessed via the python3 command).
    
Make sure to create virtual environment for Python 2 while installing OpenCV. Virtualenv is a tool to create isolated Python environments. Refer: http://pythonopencv.com/install-opencv-3-3-and-python2-7-3-5-bindings-on-ubuntu-16-04/, https://www.pyimagesearch.com/2016/10/24/ubuntu-16-04-how-to-install-opencv/

If you face isssues while installing OpenCV or running the program, try re-installing OpenCV 'WITH_JPEG=OFF' in CMAKE command this time.


# Usage
Run following code in the terminal,

`python cv-opencv-rekognition.py`

Enjoy, Have Fun!
