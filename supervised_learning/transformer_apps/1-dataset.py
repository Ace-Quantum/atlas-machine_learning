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

        en_base = []
        pt_base = []

        for en, pt in data:
            en_base.append(en.numpy().decode("utf-8"))
            pt_base.append(pt.numpy().decode("utf-8"))

        def en_iterator():
            for en in en_base:
                yield en

        def pt_iterator():
            for pt in pt_base:
                yield pt

        tokenizer_pt = transformers.BertTokenizerFast.from_pretrained(
            "neuralmind/bert-base-portuguese-cased"
        )
        tokenizer_en = transformers.BertTokenizerFast.from_pretrained(
            "bert-base-uncased"
        )

        vocab_size = 2**13

        en_model_trained = tokenizer_en.train_new_from_iterator(
            text_iterator=en_iterator(), vocab_size=vocab_size
        )

        pt_model_trained = tokenizer_pt.train_new_from_iterator(
            text_iterator=pt_iterator(), vocab_size=vocab_size
        )

        # Train here somewhere I guess
        # They need to be trained on the data passed in
        return pt_model_trained, en_model_trained


    def encode(self, pt, en):
        """Documentation"""

        pt_tokens = self.tokenizer_pt.encode(pt.numpy().decode("utf-8"))
        en_tokens = self.tokenizer_en.encode(en.numpy().decode("utf-8"))

        return pt_tokens, en_tokens
    

