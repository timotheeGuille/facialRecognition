import cv2
import time


#cam = cv2.VideoCapture(0)
cam = cv2.VideoCapture("media/ulti.mp4")
cam.set(cv2.CAP_PROP_POS_MSEC, 120000)

#haar_cascade = cv2.CascadeClassifier('data\haarcascade_frontalface_default.xml')
haar_cascade = cv2.CascadeClassifier('data\haarcascade_fullbody.xml')

prev_frame_time = 0
new_frame_time = 0
nbframe=0

while(cam.isOpened()):

    ret, img = cam.read()
    if ret == True:
        nbframe+=1
        
        cv2.imshow("cam",img)

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        
        faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.01, minNeighbors=1)

        for (x, y, w, h) in faces_rect:
            cv2.rectangle(gray_img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
  
            cv2.imshow('Detected faces', gray_img)

            
            
        #print fps 

        new_frame_time = time.time()
        fps = 1/(new_frame_time-prev_frame_time)
        prev_frame_time = new_frame_time
        
        print("nbframe=",nbframe,"  fps=",fps)


        if cv2.waitKey(20) & 0xFF == ord('q'):
            break
    else:
        break

cam.release()

cv2.destroyAllWindows()