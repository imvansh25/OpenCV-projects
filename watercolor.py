import cv2
import numpy as np
from collections import defaultdict
from scipy import stats

def watercolor_painting(img):
    res = cv2.stylization(img, sigma_s=60, sigma_r=0.6)
    return res