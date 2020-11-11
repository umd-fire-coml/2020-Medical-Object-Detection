from tensorflow.keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True)

train_generator = train_datagen.flow_from_directory(
    'data/train',
    target_size=(500, 500),
    batch_size=32,
    shuffle=True,
    class_mode='binary',
    subset='training')

test_generator = test_datagen.flow_from_directory(
    'data/test',
    target_size=(500, 500),
    batch_size=32,
    shuffle=True,
    class_mode='binary')
