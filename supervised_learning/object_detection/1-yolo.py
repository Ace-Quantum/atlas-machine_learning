#!/usr/bin/env python3

"""Set up for the Yolo Model"""

from tensorflow import keras as K
import numpy as np


def load_class_names(filepath):
    """Load up the classes"""
    with open(filepath, "r") as file:
        class_names = file.readlines()
    return [name.strip() for name in class_names]


class Yolo:
    """Yolo Class"""

    def __init__(self, model_path, classes_path, class_t, nms_t, anchors):
        """initialization of yolo"""
        self.model = K.models.load_model(model_path)
        self.class_names = load_class_names(classes_path)
        self.class_t = class_t
        self.nms_t = nms_t
        self.anchors = anchors

    def process_outputs(self, outputs, image_size):
        """Processes the outputs"""
        # Pull the dimensions of the image
        image_height, image_width = image_size

        # make lists to hold outputs
        boxes = []
        box_confidences = []
        box_class_probs = []

        # for each output
        for output in outputs:
            # Grab box coordinates
            processed_boxes = output[:, :, :, :4]

            # convert coordinates
            processed_boxes[..., :2] = (processed_boxes[..., :2] + np.indices((
                output.shape[0], output.shape[1])).T) / (output.shape[0], output.shape[1])
            
            processed_boxes[..., 2:4] = np.exp(processed_boxes[..., 2:4]) * self.model.anchors / image_size

            # extract confidences
            box_confidence = output[:, :, :, 4:5]

            # extract class probabilities
            box_class_prob = output[:, :, :, 5:]

            boxes.append(processed_boxes)
            box_confidences.append(box_confidence)
            box_class_probs.append(box_class_prob)

        return boxes, box_confidences, box_class_probs
