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
        # grab variables
        image_h, image_w = image_size
        input_h, input_w = self.model.input.shape[1:3]

        # make lists to hold outputs 
        boxes = []
        box_confidences = []
        box_class_probs = []

        # for each output
        for index, output in enumerate(outputs):

            # debug print because I'm going insane
            # print(f"shape of output[..., :4]: {output[..., :4].shape}")

            # Grab grid params
            grid_h, grid_w, anch_boxes = output.shape[:3]
            box_cords = output[..., :4]

            # Confidences and probabilities
            box_confidence = self.sigmoid(output[..., 4:5])
            box_class_prob = self.sigmoid(output[..., 5:])

            box_confidences.append(box_confidence)
            box_class_probs.append(box_class_prob)

            # Trying a different approach I've seen
            for i in range(grid_h):
                for j in range(grid_w):
                    for anch_idx in range(anch_boxes):
                        # Initializing values
                        anch_w, anch_h = self.anchors[index][anch_idx]
                        tx, ty, tw, th = box_cords[i, j, anch_idx]

                        # get boundary box center coordinates
                        bound_box_x = (self.sigmoid(tx) + j)
                        bound_box_y = (self.sigmoid(ty) + i)

                        # get width and height
                        bound_box_w = anch_w * np.exp(tw)
                        bound_box_h = anch_h * np.exp(th)

                        # normalization
                        bound_box_x /= grid_w
                        bound_box_y /= grid_h
                        bound_box_w /= int(input_w)
                        bound_box_h /= int(input_h)

                        # conversion to scale
                        tl_x = bound_box_x - (bound_box_w / 2)
                        tl_y = bound_box_y - (bound_box_h / 2)
                        lr_x = bound_box_x + (bound_box_w / 2)
                        lr_y = bound_box_y + (bound_box_h / 2)
                        box_cords[i, j, anch_idx] = [tl_x, tl_y, lr_x, lr_y]

            boxes.append(box_cords)

        return boxes, box_confidences, box_class_probs
