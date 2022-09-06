import cv2
import f_liveness_detection
import cv2
import numpy as np
import imutils
import time
COUNTER,TOTAL = 0,0

if __name__ == "__main__":
    im = cv2.imread("data_test/friends1.jpg")
    im = imutils.resize(im, width=720)
    out = f_liveness_detection.detect_liveness(im,COUNTER,TOTAL)
    print(out)