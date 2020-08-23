import numpy as np

def dodge(front,back):
    result=front*255/(255-back) 
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')



def grayscale(rgb):
    return np.dot(rgb[...,:3], [0.299, 0.587, 0.114])


def scanned_image(s):
	g=grayscale(s)
	i = 255-g
	import scipy.ndimage
	b = scipy.ndimage.filters.gaussian_filter(i,sigma=20)
	r= dodge(b,g)
	return r





