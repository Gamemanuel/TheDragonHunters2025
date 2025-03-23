import cv2
import numpy as np

from cscore import CameraServer as CS


def main():
    CS.enableLogging()
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        width = int(cap.get(3))
        height = int(cap.get(4))

        cv2.imshow('frame')
    