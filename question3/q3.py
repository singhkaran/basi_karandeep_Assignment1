from __future__ import division
import sys
import math
import Image
import ImageDraw
from scipy.spatial import distance
import PIL.ImageOps 
from scipy import signal
from scipy import misc
import numpy as np
from scipy.misc import imread
from scipy import ndimage

# This recurrence is quicker but loses accuracy dramatically when v > 9
def besselRecurrence(v, x):
	if v == 0 or v == 1:
		return besselApprox(v, x)
	else:
		return (2 * (v - 1) / x) * besselRecurrence(v - 1, x) - besselRecurrence(v - 2, x)

#Slower calculation but more accurate than recurrence
def besselApprox(v, x):
	sum = 0.0
	for k in range(0, 10):
		numerator =  math.pow(-1, k) * math.pow(x / 2, v + (2 * k))
		denominator = math.factorial(k) * math.factorial(v + k)
		sum += (numerator / denominator)
	return sum

# source for approximation and recurrence http://www.mhtlab.uwaterloo.ca/courses/me755/web_chap4.pdf

# a - radius of telescope, q - pattern of intensity seen in focal plane at distance q
# R - distance from aperature to focal plane
def calculateIntensity(a, q, wavelength, R):
	x = (math.pi * 2 * a * q) / (wavelength * R)
	return math.pow(2 * besselApprox(1, x) / x, 2)

# Create a point spread image

def createPointSpreadImage():
	image = Image.new("L", [256, 256])

	origin = (128, 128)

	for i in range (0, 256):
		for j in range (0, 256):
			if (i, j) == origin:
				continue
			R = math.sqrt(math.pow(128 - i, 2) + math.pow(128 - j, 2))
			# PIL has a problem with long ints, need to force them to stay black without calculating
			if (R < 7):
				continue
			intensity = calculateIntensity(1, 1, 1, R / 10)
			image.putpixel((i, j), intensity * 255)
	invert = PIL.ImageOps.invert(image)
	return invert

def convolveImages(picPath, outputPath):
	pointSpread = createPointSpreadImage().convert("RGB")
	spacePic = Image.open(picPath)
	blurred = signal.fftconvolve(np.asarray(pointSpread), np.asarray(spacePic), mode="same")
	misc.imsave(outputPath, blurred)

