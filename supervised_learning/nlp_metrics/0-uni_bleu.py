#!/usr/bin/env python3
"""manual transition is just when you use the command line rather than HRT"""

import numpy as np

def uni_bleu(references, sentence):
    """You need references for uni"""

    sentence_counts = {}
    for word in sentence:
        sentence_counts[word] = sentence_counts.get(word, 0) + 1

    max_ref_counts = {}
    for reference in references:
        for word in reference:
            max_ref_counts[word] = max(max_ref_counts.get(word, 0), reference.count(word))

    clipped_count = 0
    for word in sentence_counts:
        clipped_count += min(sentence_counts[word], max_ref_counts.get(word, 0))

    precision = clipped_count / len(sentence)

    sentence_len = len(sentence)
    ref_lengths = [len(ref) for ref in references]
    closest_ref_len = min(ref_lengths, key=lambda ref_len: (abs(ref_len - sentence_len), ref_len))

    if sentence_len > closest_ref_len:
        brevity_penelty = 1
    else:
        brevity_penelty = np.exp(1 - closest_ref_len / sentence_len)

    bleu_score = brevity_penelty * precision

    return bleu_score
