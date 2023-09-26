import os
import cv2


path = "Images/"


images = []

#Taking the pictures one by one. Putting in image list
 
for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
print(len(images))
count = len(images)

#Reading the images, height width and chanels in variables

frame = cv2.imread(images[0])
height, width, channels = frame.shape
size = (width, height)


#Applying settings to video. (video name, codec, # of pictures per frame, WidthXHeight)
out = cv2.VideoWriter('Project.avi', cv2.VideoWriter_fourcc(*'DIVX'), 0.8, size)


for i in range(0,count-1):
    frame = cv2.imread(images[i])
    out.write(frame)


#Releasing the video generated
out.release()
print("Done")

