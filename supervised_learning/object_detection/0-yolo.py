#!/usr/bin/env python3

from tensorflow import keras as K

def load_class_names(filepath):
    with open(filepath, 'r') as file:
        class_names = file.readlines()
    return [name.strip() for name in class_names]

class Yolo:
    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        self.model = K.models.load_model(model_path)
        self.class_names = load_class_names(classes_path)
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors
