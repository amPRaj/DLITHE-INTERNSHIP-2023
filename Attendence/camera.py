import cv2
import random

camera=cv2.VideoCapture(0)

while(True):
    flag,image=camera.read()
    cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # image=cv2.imread('./dataset/0/myimage19.jpeg')
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    # print(type(image),type(flag))
    faces=cascade.detectMultiScale(gray,1.1,5)
    if len(faces)==0:
        print("Nobody in the room, turning off light")
    else:
        print("somebody in the room,turning on light")
    print(faces)

    for x,y,w,h in faces:
        cv2.rectangle(image,(x,y),(x+w,y+h),(255,255,0),2)
    cv2.imshow("Mycam",image)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break

    if k==ord('s'):
        index=random.randint(1,100) 
        crop=image[y:y+h,x:x+w]
        filename=f"./dataset/1/myimage{index}.jpeg"
        cv2.imwrite(filename,crop)

camera.release()