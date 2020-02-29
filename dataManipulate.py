# importing packages
import pandas as pd
import csv
#import numpy as np
import PIL
from PIL import Image
import os
import random
#import matplotlib

# Loading training csv into pandas


labelsPath = "D:\\Health Project\\TEST\\trainTEST.csv"
imageFolder = "D:\\Health Project\\TEST\\Train Images_Unzipped"
# loading csv into pandas


df_trainSec = pd.read_csv(labelsPath)

# Sort pandas by idcode, store list of labels
df_trainSec.sort_values(by=['id_code'])
print("lol")
print(df_trainSec['id_code'])
print("lol")
#
list_of_labels = df_trainSec["diagnosis"].tolist()

# image id is list of id codes
imageid = df_trainSec['id_code']
# print(imageid[0])

# loading training images
imagesPath = imageFolder
# print(os.listdir(imagesPath))
imageNames = os.listdir(imagesPath)
# imageNames.remove('.DS_Store')
imageNames.sort()

# print(imageNames[0])


def manipulateImage(imgPath, newName, diag):
    print('replicating..')

    im = Image.open(imgPath)

    # gets random integer in between 1 and 4
    num = random.randint(45,305)
    edited_image = im.rotate(num)

    # # Rotate 180
    # elif (num==2):
    #     edited_image = im.rotate(180)

    # # reflect vertically
    # elif (num==3):
    #     edited_image = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)

    # elif (num==4):
    #     edited_image = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    # elif (num==5):
    #     edited_image = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)
    

    # add newly created image to pandas
    addToCSV(newName, diag)
    print(newName)
    edited_image.save("D:\\Health Project\\TEST\\NewImages\\" + newName+".png")



# Function to add to pandas
def addToCSV(newName, diag):
    fields = [newName, str(diag)]
    with open(labelsPath, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)


# Image manipulation
# This loops through the list of labels, trying to create equivalent number of images for each label (around 2000)
# if label is 1, create one copy of image
# If label is 2, create 3 more copies of image
# if label is 3, create eight more copies of image
# If label is 4, create 7 more copies of each image

# len(list_of_labels)
OneFrequency = 1
TwoFrequency = 3
ThreeFrequency = 8
FourFrequency = 8     

for i in range(len(list_of_labels)):
    print(imageid[i])
    print(list_of_labels[i])

    if list_of_labels[i] == 1:
        for j in range(OneFrequency):
            imageName = "1" + imageid[i] + str(i)
        #Arguments: path to image, image name (diagnosislabel, imageid, uniquenum)
            print(i)
            manipulateImage(imagesPath + '\\' + imageNames[i], imageName, 1)

    elif list_of_labels[i] == 2:

        for j in range(TwoFrequency):
            
            imageName = "2" + imageid[i] + str(j) + ".png"
            manipulateImage(imagesPath + '\\' + imageNames[i], imageName, 2)

    elif list_of_labels[i] == 3:

        for j in range(ThreeFrequency):
            imageName = "3" + imageid[i] + str(j) + ".png"
            manipulateImage(imagesPath + '\\' + imageNames[i], imageName, 3)

    elif list_of_labels[i] == 4:

        for j in range(FourFrequency):
            imageName = "4" + imageid[i] + str(j) + ".png"
            manipulateImage(imagesPath + '\\' + imageNames[i], imageName, 4)
