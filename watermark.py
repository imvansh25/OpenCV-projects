#Import required Image library
from PIL import Image, ImageDraw, ImageFont
import cv2
import numpy as np
import matplotlib.pyplot as plt


def watermark1(img_name,text,size,name):
	#Create an Image Object from an Image
	im = Image.open(img_name)
	width, height = im.size

	draw = ImageDraw.Draw(im)

	font = ImageFont.truetype('arial.ttf', size)
	textwidth, textheight = draw.textsize(text, font)

	# calculate the x,y coordinates of the text
	margin = 10
	x = width - textwidth - margin
	y = height - textheight - margin

	# draw watermark in the bottom right corner
	draw.text((x, y), text, font=font)

	#Save watermarked image
	im.save(name)

def watermark2(img_name,text,name,size):
	img1 = cv2.imread(img_name)
	img_rgb = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
	blank_img = np.zeros(shape=(img_rgb.shape[0],img_rgb.shape[1],3), dtype=np.uint8)
	font = cv2.FONT_HERSHEY_SIMPLEX  
	cv2.putText(blank_img,  
	            text=text,  
	            org=(img_rgb.shape[1]//8, img_rgb.shape[0]//2),   
	            fontFace=font,  
	            fontScale= size,color=(255,255,255),  
	            thickness=10,  
	            lineType=cv2.LINE_4)
	blended = cv2.addWeighted(src1=img_rgb,alpha=0.7,src2=blank_img,beta=1, gamma = 0)
	cv2.imwrite(name, cv2.cvtColor(blended, cv2.COLOR_RGB2BGR))
