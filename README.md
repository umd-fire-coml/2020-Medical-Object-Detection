# The Model:
 - The model will take the preprocessed images from the input pipeline and trains itself to learn which are benign and which are malignant
 - We used a Convolutional Neural Network, which is specific for image clssification
 - The model has multiple layers for input and output, shown below
 ```
visible = Input(shape=(500, 500,3))
conv1 = Conv2D(32, kernel_size=4, activation='relu')(visible)
pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
conv2 = Conv2D(16, kernel_size=4, activation='relu')(pool1)
pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
flat = Flatten()(pool2)
hidden1 = Dense(10, activation='relu')(flat)
output = Dense(1, activation='sigmoid')(hidden1)

model = Model(inputs=visible, outputs=output)
 ```
  - Once we have our layers we compiled the model:
  ```
  model.compile(
    optimizer=RMSprop(),
    loss=tf.keras.losses.BinaryCrossentropy(),
    metrics=["accuracy"],
)
  ```
  - Then, we trained the model and saved the weights we created