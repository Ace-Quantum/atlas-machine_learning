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
        # Pull the dimensions of the grid, the number of anchors, and the number of classes
        # We may not need the last two.
        grid_height, grid_width = outputs[0].shape[:2]
        # num_anchors = outputs[0].shape[2]
        # num_classes = outputs[0].shape[-1] - 5

        # make lists to hold outputs
        boxes = []
        box_confidences = []
        box_class_probs = []

        # for each output
        for output in outputs:

            # debug print because I'm going insane
            print(f"shape of output[..., :4]: {output[..., :4].shape}")

            # Grab grid params
            # tx, ty, tw, th = output[..., :4]
            box_cords = output[..., :4]
            # print(f"output 4: {output[..., :4]}")

            # Confidences and probabilities
            box_confidence = self.sigmoid(output[..., 4:5])
            box_class_prob = self.sigmoid(output[..., 5:])

            box_confidences.append(box_confidence)
            box_class_probs.append(box_class_prob)

            # grid centers (I don't understand this part)
            grid_x_center = np.linspace(0, image_size[1], grid_width)
            grid_y_center = np.linspace(0, image_size[0], grid_height)

            # bounding box centers
            bx_center = (box_cords[0] * grid_x_center[:, :, None] + (1 - box_cords[0]) * (grid_x_center + 1))[:, :, None]
            by_center = (box_cords[1] * grid_y_center[:, :, None] + (1 - box_cords[1]) * (grid_y_center + 1))[:, :, None]

            # box widths and heights
            bw = box_cords[2] * np.exp(box_cords[0]) * (grid_x_center[:, :, None] + 1)
            bh = box_cords[3] * np.exp(box_cords[1]) * (grid_y_center[:, :, None] + 1)

            # Convert Corners
            top_left = np.concatinate([bx_center - .5 * bw, by_center - .5 * bh], axis=-1)
            bottom_right = np.concatenate([bx_center + .5 * bw, by_center + .5 * bh], axis=-1)

            # Reshape
            top_left = np.transpose(top_left, (2, 0, 2))
            bottom_right = np.transpose(bottom_right, (2, 0, 1))

            boxes.append(np.concatenate([top_left, bottom_right], axis=-1))

        return boxes, box_confidences, box_class_probs
