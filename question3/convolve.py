import q3
import sys

# handle input as args (ex - q3.py FileToConvolve SaveLocation)
picPath = sys.argv[1]
outputPath = sys.argv[2]

q3.convolveImages(picPath, outputPath)
