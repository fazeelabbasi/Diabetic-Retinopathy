# importing packages
import pandas as pd
import csv
import numpy as np
import PIL
from PIL import Image
import os
import random

import matplotlib

# Loading training csv into pandas
path = os.getcwd();
labelsPath = path + '\\train.csv'

# loading csv into pandas
df_trainSec = pd.read_csv(labelsPath)

# Sort pandas by idcode, store list of labels
df_trainSec.sort_values(by=['id_code'])

#
list_of_labels = df_trainSec["diagnosis"].tolist()

# image id is list of id codes
imageid = df_trainSec['id_code']
# print(imageid[0])
# loading training images
imagesPath = path + '\\Train Images_Unzipped'
imageNames = os.listdir(imagesPath)
imageNames.sort()
# print(imageNames[0])
from PIL import Image


def manipulateImage(imgPath, newName, diag):
    print(newName)

    im = Image.open(imgPath)

    # gets random integer in between 1 and 5
    num = random.randint(1, 4)

    # Rotate 90
    if (num == 1):
        edited_image = im.rotate(90)

    # Rotate 180
    elif (num == 2):
        edited_image = im.rotate(180)

        # reflect vertically
    elif (num == 3):
        edited_image = im.transpose(PIL.Image.FLIP_TOP_BOTTOM)

    elif (num == 4):
        edited_image = im.transpose(PIL.Image.FLIP_LEFT_RIGHT)

    # add newly created image to pandas
    addToPandas(newName, diag)
    print(df_trainSec.head(3))

    edited_image.save("C:\\Users\\Fazeel\\Desktop\\Qmind\\savefile" ,newName)


# Function to add to pandas
def addToPandas(newName, diag):
    # creating
    df2 = pd.DataFrame({"id_code": [newName], "diagnosis": [diag]})

    global df_trainSec
    df_trainSec = df_trainSec.append(df2, ignore_index=True)


# Image manipulation
# This loops through the list of labels, trying to create equivalent number of images for each label (around 2000)
# if label is 1, create one copy of image
# If label is 2, create 3 more copies of image
# if label is 3, create eight more copies of image
# If label is 4, create 7 more copies of each image

# len(list_of_labels)
for i in range(len(list_of_labels)):

    if list_of_labels[i] is 1:
        imageName = "1" + imageid[i] + str(i) + ".png"

        #       Arguments: path to image, image name (diagnosislabel, imageid, uniquenum)
        manipulateImage(imagesPath + '/' + imageNames[i], imageName, 1)

    elif list_of_labels[i] is 2:

        for j in range(3):
            imageName = "2" + imageid[i] + str(j) + ".png"
            manipulateImage(imagesPath + '/' + imageNames[i], imageName, 2)

    elif list_of_labels[i] is 3:

        for j in range(8):
            imageName = "3" + imageid[i] + str(j) + ".png"
            manipulateImage(imagesPath + '/' + imageNames[i], imageName, 3)

    elif list_of_labels[i] is 4:

        for j in range(8):
            imageName = "4" + imageid[i] + str(j) + ".png"
            manipulateImage(imagesPath + '/' + imageNames[i], imageName, 4)

# Practising image manipulation

# im = Image.open(imagesPath + '/' + imageNames[0])
# width, height = im.size
# width
# # height
# im.show
