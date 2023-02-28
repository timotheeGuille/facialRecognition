import cv2

cam = cv2.VideoCapture(0)

haar_cascade = cv2.CascadeClassifier('data\haarcascade_frontalface_default.xml')

while(cam.isOpened()):

    ret, img = cam.read()
    if ret == True:
        
        cv2.imshow("cam",img)

        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        
        faces_rect = haar_cascade.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=9)

        for (x, y, w, h) in faces_rect:
            cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)
  
            cv2.imshow('Detected faces', img)


        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    else:
        break

cam.release()

cv2.destroyAllWindows()