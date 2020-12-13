# 2020-Medical-Object-Detection

This repository contains a neural network that is able to detect melanoma, a serious type of skin cancer.

This type of cancer can be easily confused with skin discoloration, so being able to notice what is skin cancer and benign skin discoloration is extremely important.

![Melanoma vs Benign](https://chcsga.org/wp-content/uploads/2019/05/d.jpg)

As seen in the above images, melanoma can be extremely difficult to detect just based off of the human eye, so machine learning can provide an essential tool to help detect a life-threatening disease.

Below is a Google Drive link to the dataset:

https://drive.google.com/drive/folders/1yK2W4D9y3VdnIg5SoDeGAWD1e1rSAKGp?usp=sharing

The dataset is formatted in the following way:

ISBI2016_ISIC_Part3_Training_Data

 -test
 
    -benign
    
    -malignant
 -train
 
    -benign
    
    -malignant
    
Instructions to move data to "My Drive" in Google Drive:

1. Sign in to the Google account you want the data downloaded to
2. Access the link, and make sure the folder is in the "Shared with Me" section
3. Click on the folder and use the keyboard command "Shift + Z"
4. A menu will pop up. This menu will allow you to choose where you want the directory moved to. Select "My Drive".
The data should now be in the "My Drive" section. This will allow you to run the data generator, which will allow you to train the model.

Data Generator:
Generates data from the dataset to feed to the model
Makes it possible to handle large amounts of data
Uses Image Data Generator which allows augmentation and preparation of images for image classification in the model
Uses tensorflow flow from directory to generate batches of train and test data

Input Pipeline:
The pipeline will feed batches of data from the data generator into the model
Prefetches and processes next batch of data as it's feeding in the current batch into the model
The following code will create the pipeline, taking data from the data generator
pipe = tf.data.Dataset.from_generator(
       lambda: generator, 
       output_types=(tf.float32, tf.float32),
       output_shapes=([1,150,150,3], [1,]))
       
Next, we will modify the images in each batch using the map function and a modify function we created
pipe.map (lambda x,y : modify(x,y))

Then, we run the prefetch method to create a dataset that will prefetch the next batch as the current data is processed
pipe.prefetch(batch_size)

This is the most important parts of the pipeline, allowing us to fetch data from the data generator and prefetch the next batch as we're processing the current data, decreasing idle time and increasing efficiency

The Model:
The model will take the preprocessed images from the input pipeline and trains itself to learn which are benign and which are malignant
We used a Convolutional Neural Network, which is specific for image clssification
The model has multiple layers for input and output, shown below
visible = Input(shape=(500, 500,3))
conv1 = Conv2D(32, kernel_size=4, activation='relu')(visible)
pool1 = MaxPooling2D(pool_size=(2, 2))(conv1)
conv2 = Conv2D(16, kernel_size=4, activation='relu')(pool1)
pool2 = MaxPooling2D(pool_size=(2, 2))(conv2)
flat = Flatten()(pool2)
hidden1 = Dense(10, activation='relu')(flat)
output = Dense(1, activation='sigmoid')(hidden1)

model = Model(inputs=visible, outputs=output)
Once we have our layers we compiled the model:
model.compile(
  optimizer=RMSprop(),
  loss=tf.keras.losses.BinaryCrossentropy(),
  metrics=["accuracy"],
)

Then, we trained the model and saved the weights we created
num_epochs = 5 #You can increase or decrease this number depending on how long you want to train for
if (path.isfile('/content/gdrive/My Drive/ISBI2016_ISIC_Part3_Training_Data/model weights/model.h5')):
    #You can change the path of "model.h5" to wherever you want to save/load the weights
    print("Model doesn't currently exist, creating new one.")
    history = model.fit(pipeline(train_generator), batch_size=32, steps_per_epoch=100, epochs=num_epochs)
    model.save_weights("/content/gdrive/My Drive/ISBI2016_ISIC_Part3_Training_Data/model weights/model.h5")
else:
    model.load_weights("/content/gdrive/My Drive/ISBI2016_ISIC_Part3_Training_Data/model weights/model.h5")
    history = model.fit(pipeline(train_generator), batch_size=32, steps_per_epoch=100, epochs=num_epochs)
    model.save_weights("/content/gdrive/My Drive/ISBI2016_ISIC_Part3_Training_Data/model weights/model.h5")
    
Explanation Video: https://youtu.be/00TLCkC91vE

Interactive Model: https://colab.research.google.com/drive/1e1LFupI_S8jD0LTI5V1DpMQQckAgqjsM?usp=sharing
