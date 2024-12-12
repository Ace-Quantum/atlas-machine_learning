#!/usr/bin/env python3
"""Class for a dataset"""
# https://huggingface.co/learn/nlp-course/en/chapter2/4
# ^^ Tokenizer from the transformers library
# We're encouraged to use huggingface
# Which sounds like a library based on a horror movie

#   Nope, nevermind
#   It gives us the exact ones it wants
#   Which is the one we use
#   In the case of using the bertuguese tokenizer that I had found

#       Double nope!! It is in fact the link I had written first
#       There was a different resource I had gotten confused with

import transformers
import tensorflow_datasets as tfds


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
        tokenizer_pt = transformers.BertTokenizer.from_pretrained(
            "neuralmind/bert-base-portuguese-cased"
        )
        tokenizer_en = transformers.BertTokenizer.from_pretrained(
            "bert-base-uncased")

        return tokenizer_pt, tokenizer_en
