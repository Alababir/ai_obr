import cv2
import time
import numpy as np

from csv import DictWriter

camera = cv2.VideoCapture(0)
h, w = None, None

with open("yoloDados/YoloNames.names") as f:
    labels = [line.strip() for line in f]

network = cv2.dnn.readNetFromDarknet("yoloDados/yolov3.cfg",
                                     "yoloDados/yolov3.wights")

layers_names_all = network.getLayerNames()

layers_names_output = \
    [layers_names_all[i[0] - 1] for i in network.getUnconnectedOutLayers()]
