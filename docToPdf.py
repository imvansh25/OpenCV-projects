from docx2pdf import convert
from PIL import Image
import os

def convertDocxToPdf(input_path,output_name):

	dir_path = os.path.dirname(os.path.realpath(__file__))
	output_path = dir_path+"/"+output_name
	convert(input_path, output_name)
	return output_name

def convertJpgToPng(input_path,output_path):
    imjpg = Image.open(input_path)
    imjpg.save(output_path)
    return output_path


def convertPngToJpg(input_path, output_path):
    impng = Image.open(input_path)
    impng.save(output_path)
    return output_path
