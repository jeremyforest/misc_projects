## from sentdex https://www.youtube.com/watch?v=wQ8BIBpya2k

import tensorflow as tf



mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

## normalization of the data
x_train = tf.keras.utils.normalize(x_train, axis = 1)
x_test = tf.keras.utils.normalize(x_test, axis = 1)


model = tf.keras.models.Sequential()
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(128, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(10, activation=tf.nn.softmax))

model.compile(optimizer='adam', loss="sparse_categorical_crossentropy", metrics=['accuracy'])
model.fit(x_train, y_train, epochs=3)

val_loss, val_acc = model.evaluate(x_test, y_test)
print(('the validation loss is {} and validation accuracy {}').format(val_loss, val_acc))

model.save('essai1')
new_model = tf.keras.models.load_model('essai1')
prediction = new_model.predict([x_test])

import numpy as np
print(np.argmax(prediction[0]))

import matplotlib.pyplot as plt
plt.imshow(x_test[0])
plt.show()
