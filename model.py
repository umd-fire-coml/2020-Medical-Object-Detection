# Convolutional Neural Network
from keras.utils import plot_model
from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers.convolutional import Conv2D
from keras.layers.pooling import MaxPooling2D
from keras.optimizers import RMSprop
import os.path
from os import path
import matplotlib.pyplot as plt
import data_generator
import pipeline

#Layers and Output
visible = Input(shape=(500, 500,3))
conv1 = Conv2D(32, kernel_size=4, activation='relu')(visible)
pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
conv2 = Conv2D(16, kernel_size=4, activation='relu')(pool1)
pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
flat = Flatten()(pool2)
hidden1 = Dense(10, activation='relu')(flat)
output = Dense(1, activation='sigmoid')(hidden1)

model = Model(inputs=visible, outputs=output)
# summarize layers
print(model.summary())

# training
num_epochs = 5
model.compile(
    optimizer=RMSprop(),
    loss=tf.keras.losses.BinaryCrossentropy(),
    metrics=["accuracy"],
)
if not (path.isfile('model.h5')):
    print("Model doesn't currently exist, creating new one.")
    history = model.fit(pipeline(train_generator), batch_size=32, steps_per_epoch=100, epochs=num_epochs)
    model.save_weights("model.h5")
else:
    model.load_weights("model.h5")
    history = model.fit(pipeline(train_generator), batch_size=32, steps_per_epoch=100, epochs=num_epochs)
    model.save_weights("model.h5")