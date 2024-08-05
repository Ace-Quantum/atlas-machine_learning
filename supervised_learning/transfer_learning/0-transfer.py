#!/usr/bin/env python3

import tensorflow as tf
from tensorflow import keras as K

# Hey um
# What even is this?
# Like how does this work and why?
def preprocess_data(X, Y):
    """
    pre-processes the CIFAR10 dataset
    """
    X = K.applications.densenet.preprocess_input(X)
    Y = K.utils.to_categorical(Y)
    return X, Y

# Loading the dataset
(x_train, y_train), (x_test, y_test) = K.datasets.cifar10.load_data()

# Call for the preprocessing
x_train, y_train = preprocess_data(x_train, y_train)
x_test, y_test = preprocess_data(x_test, y_test)

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

output = model.layers[-1].output

# So is this just like. referencing the output of the last layer
# I mean that makes sense
# But I didn't know we could just .output it
flatten = K.layers.Flatten()
output = flatten(output)
# output = model.layers[-1].output

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

# Initialize model
model = K.models.Model(inputs=input_tensor, outputs=output)

model.compile(optimizer=K.optimizers.Adam(learning_rate=1e-4),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.save('cifar10.h5')

train_datagen = K.preprocessing.image.ImageDataGenerator(horizontal_flip=True)

train_generator = train_datagen.flow(x_train, y_train, batch_size=32)

val_datagen = K.preprocessing.image.ImageDataGenerator(horizontal_flip=True)

val_generator = val_datagen.flow(x_test, y_test, batch_size=32)

train_steps_per_epoch = x_train.shape[0] // 32
val_steps_per_epoch = x_test.shape[0] // 32

history = model.fit(train_generator,
                    steps_per_epoch=train_steps_per_epoch,
                    validation_data=val_generator,
                    validation_steps=val_steps_per_epoch,
                    epochs=20,
                    shuffle=True,
                    verbose=1)
