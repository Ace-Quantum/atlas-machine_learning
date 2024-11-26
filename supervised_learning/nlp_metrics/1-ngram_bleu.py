#!/usr/bin/env python3
"""ngrams"""

import numpy as np


def ngram_bleu(references, sentence, n):
    """Tbh I hope Sajid gives us a little extra time"""

    def generate_ngrams(words, n):
        return [" ".join(words[i: i + n]) for i in range(len(words) - n + 1)]

    sentence_ngrams = generate_ngrams(sentence, n)
    sentence_ngrams_counts = {}
    for ngram in sentence_ngrams:
        sentence_ngrams_counts[ngram] = sentence_ngrams_counts.get(
            ngram, 0) + 1

    max_ref_counts = {}
    for reference in references:
        reference_ngrams = generate_ngrams(reference, n)
        reference_counts = {}

        for ngram in reference_ngrams:
            reference_counts[ngram] = reference_counts.get(ngram, 0) + 1
        for ngram in reference_counts:
            max_ref_counts[ngram] = max(
                max_ref_counts.get(ngram, 0), reference_counts[ngram]
            )

    clipped_count = 0
    for ngram in sentence_ngrams_counts:
        clipped_count += min(
            sentence_ngrams_counts[ngram], max_ref_counts.get(ngram, 0)
        )

    total_ngrams = len(sentence_ngrams)
    precision = clipped_count / total_ngrams if total_ngrams > 0 else 0

    sentence_len = len(sentence)
    ref_lengths = [len(ref) for ref in references]
    closest_ref_len = min(
        ref_lengths, key=lambda ref_len: (abs(ref_len - sentence_len), ref_len)
    )

    if sentence_len > closest_ref_len:
        brevity_penelty = 1
    else:
        brevity_penelty = np.exp(1 - closest_ref_len / sentence_len)

    bleu_score = brevity_penelty * precision

    return bleu_score
