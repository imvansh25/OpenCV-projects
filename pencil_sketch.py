import cv2
import numpy as np
from collections import defaultdict
from scipy import stats

def pencil_sketch_bw(img):
    dst_gray, dst_color = cv2.pencilSketch(img, sigma_s=60, sigma_r=0.07, shade_factor=0.05)
    return dst_gray