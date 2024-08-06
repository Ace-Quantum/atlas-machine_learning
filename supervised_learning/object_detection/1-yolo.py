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
        image_height, image_width = image_size

        boxes = []
        box_confidences = []
        box_class_probs = []

        for output in outputs:
            grid_height, grid_width, num_anchors = output.shape[:3]

            current_boxes = np.zeros((grid_height, grid_width, num_anchors, 4))
            current_box_confidences = np.zeros((grid_height, grid_width, num_anchors, 1))
            current_box_class_probs = np.zeros((grid_height, grid_width, num_anchors, output.shape[3] - 5))

            for r in range(grid_height):
                for c in range(grid_width):
                    for a in range(num_anchors):
                        tx, ty, tw, th, conf, *class_probs = output[r, c, a]

                        x1 = (tx * image_width / grid_width) - (tw / 2)
                        y1 = (ty * image_height / grid_height) - (th / 2)
                        x2 = (tx * image_width / grid_width) - (tw / 2)
                        y2 = (ty * image_height / grid_height) - (th /2)

                        current_boxes[r, c, a] = [x1, y1, x2, y2]

                        current_box_confidences[r, c, a] = conf

                        current_box_class_probs[r, c, a] = class_probs

            boxes.append(current_boxes)
            box_confidences.append(current_box_confidences)
            box_class_probs.append(current_box_class_probs)

        return boxes, box_confidences, box_class_probs
