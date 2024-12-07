#!/usr/bin/env python3
"""Class for a dataset"""

import transformers
import tensorflow_datasets as tfds
import tensorflow as tf


class Dataset:
    """class for a dataset"""

    def __init__(self):
        """More Documentation"""
        self.data_train = None
        self.data_valid = None
        self.tokenizer_pt = None
        self.tokenizer_en = None

    def load_dataset(self):
        """More Documentation"""
        self.data_train, self.data_valid = tfds.load(
            "ted_hrlr_translate/pt_to_en",
            split=["train", "validation"],
            as_supervised=True,
            with_info=False,
        )

    def tokenize_dataset(self):
        """More Documentation"""
        self.tokenizer_pt = transformers.BertTokenizer.from_pretrained(
            "neuralmind/bert-base-portuguese-cased"
        )
        self.tokenizer_en = transformers.BertTokenizer.from_pretrained(
            "bert-base-uncased"
        )

        # the tutorial I'm following calls for a pipeline for tokenization
        # So I guess we're doing that
        def tokenize_ex(pt_sentence, en_sentence):
            pt_tokens = self.tokenizer_pt.encode(
                pt_sentence.decode("utf-8"),
                max_length=512,
                padding="max_length",
                truncation=True,
            )
            en_tokens = self.tokenizer_en.encode(
                en_sentence.decode("utf-8"),
                max_length=512,
                padding="max_length",
                truncated=True,
            )
            return tf.convert_to_tensor(
                pt_tokens, dtype=tf.int32
            ), tf.convert_to_tensor(en_tokens, dtype=tf.int32)

        def tf_tokenize_ex(pt_sentence, en_sentence):
            pt_tokens, en_tokens = tf.py_function(
                func=tokenize_ex,
                inp=[pt_sentence, en_sentence],
                Tout=(tf.int32, tf.int32),
            )
            return pt_tokens, en_tokens

        self.data_train = self.data_train.map(lambda pt, en: tf_tokenize_ex(pt, en))
        self.data_valid = self.data_valid.map(lambda pt, en: tf_tokenize_ex(pt, en))

    def get_dataset(self):
        return self.data_train, self.data_valid, self.tokenizer_pt, self.tokenizer_en
