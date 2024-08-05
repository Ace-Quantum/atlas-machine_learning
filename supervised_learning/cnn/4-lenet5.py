#!/usr/bin/env python3

import tensorflow.compat.v1 as tf

tf.disable_v2_behavior()

"""Documentation"""


def lenet5(x, y):
    """Documentation"""
    initializer = tf.keras.initializers.VarianceScaling(scale=2.0)

    conv1 = tf.nn.conv2d(
        x,
        filters=tf.Variable(initializer(shape=(5, 5, 1, 6))),
        strides=[1, 1, 1, 1],
        padding="SAME",
    )

    conv1 = tf.nn.relu(conv1)

    pool1 = tf.nn.max_pool(
        conv1, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="VALID"
    )

    conv2 = tf.nn.conv2d(
        pool1,
        filters=tf.Variable(initializer(shape=(5, 5, 6, 16))),
        strides=[1, 1, 1, 1],
        padding="VALID",
    )

    conv2 = tf.nn.relu(conv2)

    pool2 = tf.nn.max_pool(
        conv2, ksize=[1, 2, 2, 1], strides=[1, 2, 2, 1], padding="VALID"
    )

    flat_shape = pool2.get_shape().as_list()
    flat = tf.reshape(pool2,
                      [-1, flat_shape[1] * flat_shape[2] * flat_shape[3]])

    # Dense Layer, 120 nodes
    fc1_weights = tf.Variable(
        initializer([flat_shape[1] * flat_shape[2] * flat_shape[3], 120])
    )
    fc1_biases = tf.Variable(tf.zeros([120]))
    fc1 = tf.nn.relu(tf.matmul(flat, fc1_weights) + fc1_biases)

    # dense layer, 84 nodes
    fc2_weights = tf.Variable(initializer([120, 84]))
    fc2_biases = tf.Variable(tf.zeros([84]))
    fc2 = tf.nn.relu(tf.matmul(fc1, fc2_weights) + fc2_biases)

    output_weights = tf.Variable(initializer([84, 10]))
    output_biases = tf.Variable(tf.zeros([10]))
    logits = tf.matmul(fc2, output_weights) + output_biases
    softmax_output = tf.nn.softmax(logits)

    loss = tf.reduce_mean(
        tf.nn.softmax_cross_entropy_with_logits_v2(logits=logits, labels=y)
    )

    train_op = tf.train.AdamOptimizer().minimize(loss)

    correct_pred = tf.equal(tf.argmax(logits, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    return softmax_output, train_op, loss, accuracy
