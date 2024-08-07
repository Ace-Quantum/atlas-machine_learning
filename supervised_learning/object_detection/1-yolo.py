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

    def sigmoid(self, x):
        """Makes a sigmoid to return
        Idk if I'll need it"""
        return 1 / (1 + np.exp(-x))

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

            # Grab grid vars
            grid_height, grid_width, anchor_boxes, _ = output.shape

            box_xy = self.sigmoid(output[..., :2])

            box_wh = np.exp(output[..., 2:4])

            box_confidence = self.sigmoid(output[..., 4:5])

            box_class_prob = self.sigmoid(output[..., 5:])

            # Creating new grid
            col = np.tile(
                np.arange(0, grid_width), grid_height).reshape(-1, grid_width)
            row = np.tile(np.arange(0, grid_height).reshape(-1, 1), grid_width)
            col = col.reshape(grid_height, grid_width, 1, 1).repeat(
                anchor_boxes, axis=-2
            )
            row = row.reshape(grid_height, grid_width, 1, 1).repeat(
                anchor_boxes, axis=-2
            )

            box_xy += np.concatenate((col, row), axis=-1)

            box_xy /= (grid_width, grid_height)
            box_wh /= self.model.input.shape[1:3]

            box_xy -= box_wh / 2

            boxes.append(np.concatenate((box_xy, box_xy + box_wh), axis=-1))
            box_confidences.append(box_confidence)
            box_class_probs.append(box_class_prob)

        # scale boxes back to the original
        for i in range(len(boxes)):
            boxes[i][..., 0] *= image_width
            boxes[i][..., 1] *= image_height
            boxes[i][..., 2] *= image_width
            boxes[i][..., 3] *= image_height

        return boxes, box_confidences, box_class_probs
