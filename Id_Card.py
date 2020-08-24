from PIL import Image, ImageDraw, ImageFilter
import numpy as np

def Two_sided(image1,image2):
	im1 = Image.open('a4.jpg')             #  791  1024
	im2 = Image.fromarray(image1)       #  474   353
	im3 = Image.fromarray(image2)
	im1 = im1.resize((791,1024))
	im2 = im2.resize((474,353))
	im3 = im3.resize((474,353))
	im1.paste(im2,(150,100))
	im1.paste(im3,(150,500))
	return np.array(im1)




