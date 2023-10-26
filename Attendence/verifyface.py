import cv2
import datetime

import apitesting as myapi
face_recog=cv2.face.LBPHFaceRecognizer_create()
face_recog.read('facemodel.yml')

cam=cv2.VideoCapture(0)
cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

names={0:"Abhi",1:"Bhavana"}
while True:
    
    flag,image=cam.read()
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    faces=cascade.detectMultiScale(gray,1.1,5)

    detected_person=""

    if len(faces) > 0:
            
        fface=faces[0]
        x,y,w,h=fface
            
        print(x,y,w,h)
            
        crop=gray[y:y+h,x:x+w]
            
            
        label,confidence=face_recog.predict(crop)
        print(f"Label = {label}, confidence = {confidence}")

    # for x,y,w,h in faces:
        
    #     cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
    #     crop=gray[y:y+h,x:x+w]
    
    #     label,confidence=face_recog.predict(crop)
    #     print(f"Label = {label}, confidence = {confidence}")

        
        if confidence<=70:
            detected_person=names[label]
            
            myapi.senddata(detected_person)

            # Save the name and timestamp to the attendance file
            # timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            # with open('attendance.txt', 'a') as f:
            #     f.write(f"{timestamp} - {detected_person}\n")
            
        else:
            detected_person="Unknown"
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
        
        cv2.putText(image,detected_person,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,0),2,cv2.LINE_AA) 
    
    cv2.imshow("Face Recognition",image)
    k=cv2.waitKey(3)
       
    print(f"Result of Prediction = {detected_person}")
    if k==ord('q'):
        break
    
cam.release()