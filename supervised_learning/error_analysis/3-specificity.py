#!/usr/bin/env python3

"""Documentation"""
import numpy as np


def specificity(confusion):
    """documentation"""
    specificity_return = []
    num_classes = confusion.shape[0]
    true_pos = np.diag(confusion)
    true_negs = np.diag(confusion)
    false_poses = np.array([np.sum(row) - tp for tp, row in zip(true_pos, confusion.T)])

    for i in range(num_classes):
        true_neg = true_negs[i]
        false_pos = false_poses[i]

        spec = true_neg / (true_neg + false_pos) if false_pos > 0 else 1
        specificity_return.append(spec)

    return specificity_return



    # # print("Num classes" + str(num_classes))

    # for i in range(num_classes):
    #     true_neg = np.diag(confusion)
    #     false_pos = np.sum(confusion, axis=0) - true_pos

    #     specs = true_neg / (false_pos + false_neg) if false_neg > 0 else 1
    #     specificity_return.append(round(specs, 8))

    # return specificity_return
