#!/usr/bin/env python3
"""Here's some documentation
I'm using code from this website as a reference
https://medium.com/@nahmed3536/
a-python-implementation-of-pca-with-numpy-1bbd3b21de2e"""

import numpy as np


def pca(X, var=0.95):
    """And some more documentation
    I genuinely don't know what I'm doing here"""

    # n, d = X.shape

    cov_matrix = np.cov(X.T)

    eigenvals, eigenvects = np.linalg.eig(cov_matrix)

    ord_of_imp = np.argsort(-eigenvals)#[::-1]

    sort_eigenvals = eigenvals[ord_of_imp]
    sort_eigenvects = eigenvects[:, ord_of_imp]

    # exp_var = sort_eigenvals / np.sum(sort_eigenvals)

    # cum_var = np.cumsum(exp_var)
    # k = np.argmax(cum_var >= var) + 1

    # k = 2
    k = int(np.sum(sort_eigenvals >= var))

    W = sort_eigenvects[:, :k]

    W = -W

    # for i in range(W.shape[1]):
    #     W[:, i] = -W[:, i]

    # Attempting to sign switch specific parts of the matrix
    # W[:, 0:2] *= -1

    return W
