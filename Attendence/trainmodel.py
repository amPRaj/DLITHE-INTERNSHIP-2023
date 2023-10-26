import os
from os import listdir
import cv2
import numpy as np

root_dir="./dataset"

features=[]
labels=[]

lbl=0

for subfolder in listdir(root_dir):
    path=f"{root_dir}/{subfolder}"
    print(f"-----{path}-----")

    for file in listdir(path):      #accessing the subfolder
        filepath=f"{path}/{file}"
        image=cv2.imread(filepath,0)

        gimage=cv2.resize(image,(100,100))
        print(gimage)
        print("*****")
        features.append(gimage)
        labels.append(lbl)

    lbl=lbl+1
print(f"Features = {features}")
print(f"Length of features = {len(features)}")

print(f"Labels = {labels}")
print(f"Length of labels = {len(labels)}")

face_recog=cv2.face.LBPHFaceRecognizer_create()
face_recog.train(features,np.array(labels))
face_recog.save("facemodel.yml")

        # cv2.imshow("image",image)
        # cv2.waitKey()