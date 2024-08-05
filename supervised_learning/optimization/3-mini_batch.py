#!/usr/bin/env python3
"""Documentation"""

shuffle_data = __import__("2-shuffle_data").shuffle_data


def create_mini_batches(X, Y, batch_size):
    """Documentation"""
    mini_batches = []
    # data = np.haystack(X, Y)
    # np.random.shuffle(data)

    # big_batch = shuffle_data(X, Y)

    X_shuf, Y_shuf = shuffle_data(X, Y)

    n_minibatches = len(X_shuf) // batch_size

    i = 0

    for i in range(n_minibatches):
        start = i * batch_size
        end = start + batch_size
        mini_batches.append((X_shuf[start:end], Y_shuf[start:end]))

    if len(X_shuf) % batch_size != 0:
        last_batch_size = len(X_shuf) - (n_minibatches * batch_size)
        mini_batches.append((
            X_shuf[-last_batch_size:], Y_shuf[-last_batch_size:]))

    return mini_batches
