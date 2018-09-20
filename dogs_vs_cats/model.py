## inspired from sentdex

import numpy as np
import os
import pickle
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
from keras.callbacks import TensorBoard
import time

pickle_in = open("X.pickle", "rb")
X = pickle.load(pickle_in)

pickle_in = open("y.pickle", "rb")
y = pickle.load(pickle_in)

X = X/255.0 ## normalization of the data

dense_layers = [0] ## tested with 1 and 2, best is 0
conv_layers = [5]  ## Tested with 1,2,3 and 5. Best is 5
conv_layer_sizes = [64] ##Tested with 16, 32, 64. Best is 64

for conv_layer in conv_layers:
    for conv_layer_size in conv_layer_sizes:
        for dense_layer in dense_layers:
                NAME = "Cats-vs-dogs-{}-conv-{}-convnodes-{}-dense".format(conv_layer, conv_layer_size, dense_layer)
                print(NAME)
                tensorboard = TensorBoard(log_dir="logs/{}".format(NAME))

                model = Sequential()

                model.add(Conv2D(conv_layer_size, (3,3), input_shape=X.shape[1:]))
                model.add(Activation('relu'))
                model.add(MaxPooling2D(pool_size=(2,2)))
                model.add(Dropout(0.25))

                for l in range(conv_layer-1):
                    model.add(Conv2D(conv_layer_size, (3,3)))
                    model.add(Activation('relu'))
                    model.add(MaxPooling2D(pool_size=(2,2)))
                    model.add(Dropout(0.25))

                model.add(Flatten())

                for _ in range(dense_layer):
                    model.add(Dense(128))
                    model.add(Activation('relu'))

                model.add(Dense(1))
                model.add(Activation('sigmoid'))

                model.compile(loss="binary_crossentropy", optimizer='adam', metrics=['accuracy'])

                model.fit(X, y, batch_size=32, validation_split=0.1, epochs=200, callbacks=[tensorboard])

model.save(NAME)
