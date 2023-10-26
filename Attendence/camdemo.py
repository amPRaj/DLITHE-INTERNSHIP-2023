import cv2
import random

camera=cv2.VideoCapture(0)
while True:
    flag,image=camera.read()

    cv2.imshow("Mycam",image)
    k=cv2.waitKey(1)
    
    if k==ord('q'):
        break

    if k==ord('s'):
        index=random.randint(1,200) 
        filename=f".dataset/anu/myimage{index}.jpeg"
        cv2.imwrite(filename,image)
camera.release()

# save the image by pressing the key and convert the image into black and white

# import cv2

# camera = cv2.VideoCapture(0)
# flag, image = camera.read()

# if flag:
#     cv2.imshow("Mycam", image)
#     cv2.waitKey(0)  # Wait for a key press

#     # Save the image
#     cv2.imwrite("captured_image.jpg", image)

#     # Convert the image to black and white
#     gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     # Display the black and white image
#     cv2.imshow("Black and White Image", gray_image)
#     cv2.waitKey(0)  # Wait for a key press

#     # Close all OpenCV windows
#     cv2.destroyAllWindows()
# else:
#     print("Failed to capture image from camera")

# # Release the camera
# camera.release()