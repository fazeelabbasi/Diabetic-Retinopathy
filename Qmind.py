from PIL import Image  # used for loading images
import numpy as np
import os  # used for navigating to image path
import imageio  # used for writing images
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.layers. normalization import BatchNormalization
from random import shuffle

Testing_dict = {}  # id: breed
naming_dict = {}  # id: breed
IMG_SIZE = 300
DIR = "D:\\Health Project\\80Gig\\Train\\train"
TEST_DIR = "D:\\Health Project\\80Gig\\Test\\test"



f = open("D:\\Health Project\\80Gig\\trainLabels.csv", "r") # big dataset
fileContents = f.read()
fileContents = fileContents.split('\n')


ft = open("D:\\Health Project\\retinopathy_solution.csv", "r") #small dataset
fileContentst = ft.read()
fileContentst = fileContentst.split('\n')


for i in range(1, len(fileContents) - 1):
    fileContents[i] = fileContents[i].split(',')
    naming_dict[fileContents[i][0]] = fileContents[i][1]  #read in big labels
    
for i in range(1, len(fileContentst) - 1):
    fileContentst[i] = fileContentst[i].split(',')
    Testing_dict[fileContentst[i][0]] = fileContentst[i][1] #read in small labels



def load_training_data():
    train_data = []
    count = 0
    for img in os.listdir(DIR):
        # label = label_img(img)
        path = os.path.join(DIR, img)

        if "DS_Store" not in path:
            img = Image.open(path)
            img = img.convert('L')
            img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
            train_data.append([np.array(img), 1])
            count += 1
            print(count)

    for j in range(1, len(naming_dict.values())):
        train_data[j][1] = list(naming_dict.values())[j]

    shuffle(train_data)
    return train_data

def load_test_data():
    train_data = []
    count = 0
    for img in os.listdir(TEST_DIR):
        # label = label_img(img)
        path = os.path.join(TEST_DIR, img)

        if "DS_Store" not in path:
            img = Image.open(path)
            img = img.convert('L')
            img = img.resize((IMG_SIZE, IMG_SIZE), Image.ANTIALIAS)
            train_data.append([np.array(img), 1])
            count += 1
            print(count)
            
    for j in range(1, len(Testing_dict.values())):
        train_data[j][1] = list(Testing_dict.values())[j]

    shuffle(train_data)
    return train_data



test_data = load_test_data()    
testImages = np.array([i[0] for i in test_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
testLabels = np.array([i[1] for i in test_data])

train_data = load_training_data()

trainImages = np.array([i[0] for i in train_data]).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
trainLabels = np.array([i[1] for i in train_data])


model = Sequential()
model.add(Conv2D(32, kernel_size = (3, 3), activation='relu', input_shape=(IMG_SIZE, IMG_SIZE, 1)))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(96, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(96, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Conv2D(64, kernel_size=(3,3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(BatchNormalization())
model.add(Dropout(0.2))
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.2))
model.add(Dense(1, activation = 'sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics = ['accuracy'])
model.fit(trainImages, trainLabels, batch_size = 64, epochs = 50, verbose = 1)
model.save("D:\\Health Project\\diabetic_retinopathy_80gig")
model.save_weights("D:\\Health Project\\diabetic_retinopathy_80gig_weights")


loss, acc = model.evaluate(testImages, testLabels, verbose = 0)
print(acc * 100)

# https://github.com/CShorten/KaggleDogBreedChallenge/blob/master/DogBreed_BinaryClassification.ipynb


#loss, acc = model.evaluate(testImages, testLabels, verbose = 0)
#print(acc * 100)



