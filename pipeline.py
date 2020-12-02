import tensorflow as tf
import numpy as np
import os
import re
import data_generator.py 

def pipeline(generator):
    pipe = tf.data.Dataset.from_generator(
        lambda: generator, 
        output_types=(tf.float32, tf.float32),
        output_shapes=([1,150,150,3], [1,]))
    
    pipe = pipe.shuffle(batch_size, reshuffle_each_iteration=True)
    pipe = pipe.batch(batch_size)
    
    def modify(img,do):
        x = np.random.randint(1,34)
        if x <= 11:
            img = tf.image.flip_left_right(img[0])
        elif x <= 22:
            img = tf.image.flip_up_down(img[0])
        elif x < 34:
            img = tf.image.rot90(img[0], k = np.random.randint(5), name=None)
        return (img,do)
    
    pipe = pipe.map (lambda x,y : modify(x,y))
    pipe = pipe.prefetch(batch_size)
    
    return pipe
