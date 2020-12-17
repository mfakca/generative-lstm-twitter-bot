import tensorflow as tf
import sys
import os



my_model = tf.keras.models.load_model("model_saved_100_epoch")
my_model.save("saved_model.h5")
print(my_model.summary())
