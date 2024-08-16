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
        boxes = [output[..., :4] for output in outputs]
        box_confidences = []
        box_class_probs = []

        image_height = image_size[0]
        image_width = image_size[1]

        input_layer = self.model.input
        input_width, input_height = input_layer.shape[1:3]

        for i, output in enumerate(outputs):

            box = output
            box_x = box[..., 0]
            box_y = box[..., 1]
            box_w = box[..., 2]
            box_h = box[..., 3]

            box_confidence = self.sigmoid(output[..., 4:5])
            box_class_prob = self.sigmoid(output[..., 5:])

            box_confidences.append(box_confidence)
            box_class_probs.append(box_class_prob)

            grid_height = box.shape[0]
            grid_width = box.shape[1]
            num_anchors = output.shape[2]

            center_x = np.arange(grid_width).reshape(1, grid_width)
            center_x = np.repeat(center_x, grid_height, axis=0)

            center_y = np.arange(grid_width).reshape(1, grid_width)
            center_y = np.repeat(center_y, grid_height, axis=0).T

            center_x = np.repeat(center_x[..., np.newaxis],
                                 num_anchors, axis=2)

            center_y = np.repeat(center_y[..., np.newaxis],
                                 num_anchors, axis=2)

            pred_x = (self.sigmoid(box_x) + center_x) / grid_width
            pred_y = (self.sigmoid(box_y) + center_y) / grid_height
            pred_w = (np.exp(box_w) * self.anchors[i, :, 0]) / input_width
            pred_h = (np.exp(box_h) * self.anchors[i, :, 1]) / input_height

            boxes[i][..., 0] = (pred_x - (pred_w / 2)) * image_width
            boxes[i][..., 1] = (pred_y - (pred_h / 2)) * image_height
            boxes[i][..., 2] = (pred_x + (pred_w / 2)) * image_width
            boxes[i][..., 3] = (pred_y + (pred_h / 2)) * image_height

            # boxes.append(box)

        return boxes, box_confidences, box_class_probs

    def filter_boxes(self, boxes, box_confidences, box_class_probs):
        """filters the output"""
        # calculating box scores
        box_scores = [box_conf * box_class for box_conf, box_class in zip(
            box_confidences, box_class_probs)]
        box_classes = [np.argmax(score, axis=-1) for score in box_scores]
        box_class_scores = [np.max(score, axis=-1) for score in box_scores]

        filtered_box_es = [box.reshape(-1, 4) for box in boxes]
        box_classes = [cls.reshape(-1) for cls in box_classes]
        box_scores = [score.reshape(-1) for score in box_class_scores]

        filtered_box_es = np.concatenate(filtered_box_es, axis=0)
        box_classes = np.concatenate(box_classes, axis=0)
        box_scores = np.concatenate(box_scores, axis=0)

        filter_mask = box_scores >= self.class_t
        filtered_box_es = filtered_box_es[filter_mask]
        box_classes = box_classes[filter_mask]
        box_scores = box_scores[filter_mask]

        return filtered_box_es, box_classes, box_scores

    def non_max_suppression(self, filtered_boxes, box_classes, box_scores):
        filtered_boxes = filtered_boxes.tolist()
        box_classes = box_classes.tolist()
        box_scores = box_scores.tolist()

        filtered_boxes = np.array(filtered_boxes)
        box_classes = np.array(box_classes)
        box_scores = np.array(box_scores)

        box_preds = []
        pred_box_classes = []
        pred_box_scores = []

        indices = np.argsort(box_scores)[::-1]

        while len(indices) > 0:
            curr_index = indices[0]
            box_preds.append(filtered_boxes[curr_index])
            pred_box_classes.append(box_classes[curr_index])
            pred_box_scores.append(box_scores[curr_index])

            curr_box = filtered_boxes[curr_index]
            remaining_boxes = filtered_boxes[indices[1:]]

            iou = self.calculate_iou(curr_box, remaining_boxes)

            indices = indices[np.where(iou < self.nms_t)[0] + 1]

        return (np.array(box_preds), np.array(pred_box_classes), np.array(pred_box_scores))
    
    def calculate_iou(self, box, boxes):
        x1 = np.maximum(box[0], boxes[:, 0])
        y1 = np.maximum(box[1], boxes[:, 1])
        x2 = np.minimum(box[2], boxes[:, 2])
        y2 = np.minimum(box[3], boxes[:, 3])

        intersection = np.maximum(0, x2 - x1) * np.maximum(0, y2 - y1)

        box_area = (box[2] - box[0]) * (box[3] - box[1])
        boxes_area = (boxes[:, 2] - boxes[:, 0]) * (boxes[:, 3] - boxes[:, 1])

        iou = intersection / (box_area + boxes_area - intersection)

        return iou