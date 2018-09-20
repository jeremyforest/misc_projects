##inspired from sentdex

import numpy as np
import os
import cv2
from tqdm import tqdm
import random
import pickle

DATADIR = "/media/jeremy/Data/CloudStation/DNN-learning/dogs_vs_cats/kagglecatsanddogs_3367a/PetImages"
CATEGORIES = ['Dog', 'Cat']

### Moved the first 16 images of each Cat and Dog folder into new Cat and Dog folders that will be used for testing.

IMG_SIZE = 100  ## image size voulu pour le redimentionnement
training_data = []

def create_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category) ## create the path to dog and the path to cat folder
        class_num = CATEGORIES.index(category) ## associate classification number to categorie : 0=dog and 1=cat

        for img in tqdm(os.listdir(path)):
            try :
                img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)  ## convert image to array
                new_img_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE)) ## resize
                training_data.append([new_img_array, class_num]) ## associate the class to the img
            except Exception as e:
                print("image problem")

create_training_data()
#print(len(training_data))

## shuffling the data
random.shuffle(training_data)

## organizing data for model
X = []
y = []

for features, label in training_data:
    X.append(features)
    y.append(label)
X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
## save the data under this form

pickle_out = open("X.pickle", "wb")
pickle.dump(X, pickle_out)
pickle_out.close()

pickle_out = open("y.pickle", "wb")
pickle.dump(y, pickle_out)
pickle_out.close()
