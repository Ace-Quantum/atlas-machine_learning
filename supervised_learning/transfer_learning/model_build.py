#!/usr/bin/env python3

import tensorflow as tf
import tensorflow.keras as K

# Set up the initializer and the starter tensor
initializer = K.initializers.he_normal()
input_tensor = K.Input(shape=(32, 32, 3))

# Resizing
# Will need to use a different function for this
resized_images = K.layers.Lambda(lambda image: tf.image.resize(image, (224, 224)))(input_tensor)

model = K.applications.DenseNet201(include_top=False, weights='imagenet', input_tensor=resized_images,
                                   input_shape=(224, 224, 3), pooling='max', classes=1000)

# Freeze layers so we don't waste time
for layer in model.layers:
    layer.trainable = False

# So is this just like. referencing the output of the last layer
# I mean that makes sense
# But I didn't know we could just .output it
flatten = K.layers.Flatten()
output = model.layers[-1].output

layer_256 = K.layers.Dense(units=256, activation='elu', kernel_initializer=initializer,
                           kernel_regularizer=K.regularizers.l2())

output = layer_256(output)
dropout = K.layers.Dropout(0.5)

output = dropout(output)
softmax = K.layers.Dense(units=10,
                         activation='softmax',
                         kernel_initializer=initializer,
                         kernel_regularizer=K.regularizers.l2())

output = softmax(output)
cifar10 = K.models.Model(inputs=input_tensor, outputs=output)

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.save('cifar10.h5')
