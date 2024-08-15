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
        input_h, input_w = self.model.input.shape[1:3]

        # make lists to hold outputs
        boxes = []
        box_confidences = []
        box_class_probs = []

        # for each output
        for i, output in enumerate(outputs):

            # Grab grid vars
            grid_height, grid_width = output.shape[:2]
            anchors = self.anchors[i]
            num_anchors = output.shape[2]
            # print(f"anchors: {anchors}")

            # Confidences and probabilities
            box_confidence = self.sigmoid(output[..., 4:5])
            box_class_prob = self.sigmoid(output[..., 5:])

            box_confidences.append(box_confidence)
            box_class_probs.append(box_class_prob)

            # Box centers
            pred_cent = output[..., :2]
            pred_h_w = output[..., 2:4]

            # calculating normalized width and height 
            norm_box_w_h = (anchors * np.exp(pred_h_w)) / input_w
            # norm_box_w_h /= [self.model.input[0].shape[1], self.model.input[0].shape[2]]

            # calculate coordinates
            # grid = np.tile(np.indices((grid_width, grid_height)).T,
            #             anchors.shape[0]).reshape(grid_height, grid_width, -1, 2)
            
            center_x = np.arange(grid_width).reshape(1, grid_width)
            center_x = np.repeat(center_x, grid_width, axis=0)
            center_x = np.repeat(center_x[..., np.newaxis], num_anchors, axis=-1)

            center_y = np.arange(grid_height).reshape(1, grid_width)
            center_y = np.repeat(center_y, grid_width, axis=0).T
            center_y = np.repeat(center_y[..., np.newaxis], num_anchors, axis=-1)

            # grid = np.concatenate((center_x, center_y), axis=-1)
            grid = np.stack((center_x, center_y), axis=-1)
            grid = grid.reshape(pred_cent.shape)

            # print(f"shape of grid: {grid.shape}")
            # print(f"shape of pred_cent: {pred_cent.shape}")

            act_xy = (self.sigmoid(pred_cent) + grid) / [grid_width, grid_height]
            # act_xy = act_xy / [grid_width, grid_height]
            act_xy1 = (act_xy - (norm_box_w_h / 2)) * np.array([image_width, image_height])
            act_xy2 = (act_xy + (norm_box_w_h / 2)) * np.array([image_width, image_height])

            box = np.concatenate((act_xy1, act_xy2), axis=-1)

            # box *= np.tile(image_size, 2)

            boxes.append(box)


        return boxes, box_confidences, box_class_probs
