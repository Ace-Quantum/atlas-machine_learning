#!/usr/bin/env python3
"""Class for a dataset"""

import transformers
import tensorflow_datasets as tfds
import tensorflow as tf


class Dataset:
    """class for a dataset"""

    def __init__(self):
        """documentation"""
        self.data_train = tfds.load(
            "ted_hrlr_translate/pt_to_en", split="train", as_supervised=True
        )
        self.data_valid = tfds.load(
            "ted_hrlr_translate/pt_to_en",
            split="validation", as_supervised=True
        )

        self.tokenizer_pt, self.tokenizer_en = self.tokenize_dataset(
            self.data_train)

    def tokenize_dataset(self, data):
        """Documentation"""
        tokenizer_pt = transformers.AutoTokenizer.from_pretrained(
            "neuralmind/bert-base-portuguese-cased"
        )
        tokenizer_en = transformers.AutoTokenizer.from_pretrained(
            "bert-base-uncased")

        return tokenizer_pt, tokenizer_en

    def encode(self, pt, en):
        pt_tok = self.tokenizer_pt.encode(pt.)
