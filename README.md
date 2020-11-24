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

# Data Generator:
 - Generates data from the dataset to feed to the model
 - Makes it possible to handle large amounts of data
 - Uses Image Data Generator which allows augmentation and preparation of images for image classification in the model
 - Uses tensorflow flow from directory to generate batches of train and test data

# Input Pipeline:
 - The pipeline will feed batches of data from the data generator into the model
 - Prefetches and processes next batch of data as it's feeding in the current batch into the model
 - The following code will create the pipeline, taking data from the data generator
 ```
 pipe = tf.data.Dataset.from_generator(
        lambda: generator, 
        output_types=(tf.float32, tf.float32),
        output_shapes=([1,150,150,3], [1,]))
 ```
  - Next, we will modify the images in each batch using the map function and a modify function we created
  ```
  pipe.map (lambda x,y : modify(x,y))
  ```
  - Then, we run the prefetch method to create a dataset that will prefetch the next batch as the current data is processed
  ```
  pipe.prefetch(batch_size)
  ```
  - This is the most important parts of the pipeline, allowing us to fetch data from the data generator and prefetch the next batch as we're processing the current data, decreasing idle time and increasing efficiency
