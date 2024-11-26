#!/usr/bin/env python3
"""gotta go fast"""

import gensim


def fasttext_model(
    sentences,
    vector_size=100,
    min_count=5,
    negative=5,
    window=5,
    cbow=True,
    epochs=5,
    seed=0,
    workers=1,
):
    """Sanic"""

    model = gensim.models.FastText(
        sentences=sentences,
        size=vector_size,
        min_count=min_count,
        window=window,
        negative=negative,
        cbow_mean=cbow,
        hs=not cbow,
        alpha=0.025,
        min_alpha=0.001,
        seed=seed,
        workers=workers,
        epochs=epochs,
    )

    return model
