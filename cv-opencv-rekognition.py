import cv2
import numpy as np
import sys
import boto3

sys.path.append('/usr/local/lib/python2.7/site-packages/')

Bucket_Name = 'inteliot-aws'

s3 = boto3.resource('s3')

facePath = "./haarcascade_frontalface_default.xml"
smilePath = "./haarcascade_smile.xml"
faceCascade = cv2.CascadeClassifier(facePath)
smileCascade = cv2.CascadeClassifier(smilePath)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

sF = 1.05

is_looping = True

while True:

    ret, frame = cap.read() # Capture frame-by-frame
    img = frame
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor= sF,
        minNeighbors=8,
        minSize=(55, 55)
    )
    # ---- Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        smile = smileCascade.detectMultiScale(
            roi_gray,
            scaleFactor= 1.7,
            minNeighbors=22,
            minSize=(25, 25)
            )


        # Set region of interest for smiles
        for (x, y, w, h) in smile:

           print "Found", len(smile), "smiles!"
           cv2.rectangle(roi_color, (x, y), (x+w, y+h), (255, 0, 0), 1)
	   cv2.imwrite('smile_image.png', gray)
	   # Upload the captured picture to AWS Recognition for analysis
	   data = open('smile_image.png', 'rb')
	   s3.Bucket(Bucket_Name).put_object(Key='smile_image.png', Body=data)

	   if __name__ == "__main__":
	      fileName='smile_image.png'
	      bucket=Bucket_Name

	      client=boto3.client('rekognition')

	      response = client.detect_labels(Image={'S3Object':{'Bucket':bucket,'Name':fileName}},MinConfidence=75)

	      print('Detected labels for ' + fileName)
	      for label in response['Labels']:
	          print (label['Name'] + ' : ' + str(label['Confidence']))

	   cv2.waitKey(0)



    # Look at the Camera, Press ESC to capture a selfie
    cv2.imshow('Smile Detector', frame)
    c = cv2.waitKey(7) % 0x100
    if c == 27:
	break

    if not is_looping:
	cv2.waitKey(0)
	print "Found Smile"
	break

cap.release()
cv2.destroyAllWindows()
