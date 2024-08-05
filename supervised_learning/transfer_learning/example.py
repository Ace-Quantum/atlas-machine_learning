# Example Code from https://medium.com/@pierre.beaujuge/classifying-images-from-the-cifar10-dataset-with-pre-trained-cnns-using-transfer-learning-9348f6d878a8

import tensorflow as tf
import tensorflow.keras as K
import numpy as np
import matplotlib.pyplot as plt

def preprocess_data(X, Y):
    """
    function that pre-processes the CIFAR10 dataset as per
    densenet model requirements for input images
    labels are one-hot encoded
    """
    X = K.applications.densenet.preprocess_input(X)
    Y = K.utils.to_categorical(Y)
    return X, Y

# load the Cifar10 dataset, 50,000 training images
# and 10,000 test images (here used as validation data)
(x_train, y_train), (x_test, y_test) = K.datasets.cifar10.load_data()

# preprocess the data using the application's preprocess_input method and convert the labels to one-hot encodings
#   I honestly still don't know what a one-hot encoding is
x_train, y_train = preprocess_data(x_train, y_train)
x_test, y_test = preprocess_data(x_test, y_test)

# weights are initialized as per the he et al. method
initializer = K.initializers.he_normal()
input_tensor = K.Input(shape=(32, 32, 3))

# resize images to the image size upon which the networkwas pre-trained
#   I need to figure out how to do this with only Keras
resized_images = K.layers.Lambda(lambda image: tf.image.resize(image, (224, 224)))(input_tensor)
model = K.applications.DenseNet201(include_top=False,
                                   weights='imagenet',
                                   input_tensor=resized_images,
                                   input_shape=(224, 224, 3),
                                   pooling='max',
                                   classes=1000)

# make the weights and biases of the base model non-trainable
# by "freezing" each layer of the DenseNet201 network
#   Was the point of doing this not to train the model? Why freeze?
#   Kinda nice that there's a true/false value for trainable tho
for layer in model.layers:
    layer.trainable = False
output = model.layers[-1].output

# reshape the output feature map of the base model before passing the data on to the Dense layers of the classifier head
#   Is the activation supposed to be 'elu' or is that a bug to trip up plagarists?
#   I'm also kinda confused with the rest of this. 
#   I understand that it's using/placing/creating various layers
#   But I don't fully get what's happening here
flatten = K.layers.Flatten()
output = flatten(output)
layer_256 = K.layers.Dense(units=256,
                           activation='elu',
                           kernel_initializer=initializer,
                           kernel_regularizer=K.regularizers.l2())
output = layer_256(output)
dropout = K.layers.Dropout(0.5)
output = dropout(output)
softmax = K.layers.Dense(units=10,
                         activation='softmax',
                         kernel_initializer=initializer,
                         kernel_regularizer=K.regularizers.l2())
output = softmax(output)
model = K.models.Model(inputs=input_tensor, outputs=output)