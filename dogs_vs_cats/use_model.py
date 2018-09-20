##inspired from sentdex

import cv2
import tensorflow as tf
import keras
import os


DATADIR = "/media/jeremy/Data/CloudStation/DNN-learning/dogs_vs_cats/out_of_sample_pictures"
CATEGORIES = ['Dog', 'Cat']

#import pdb; pdb.set_trace()

img_paths = []
for i in os.listdir(DATADIR):
    path = os.path.join(DATADIR, i)
    img_paths.append(path)

def prepare_new_data(img):
    IMG_SIZE = 100
    img_array = cv2.imread(img, cv2.IMREAD_GRAYSCALE)
    new_img_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_img_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


model = keras.models.load_model("/media/jeremy/Data/CloudStation/DNN-learning/dogs_vs_cats/Cats-vs-dogs-5-conv-64-convnodes-0-dense")

for image in img_paths:
    prediction = model.predict([prepare_new_data(image)])
    print("prediction for image {} is a {}".format(image, CATEGORIES[int(prediction[0][0])]))
