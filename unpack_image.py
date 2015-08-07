from PIL import Image

inputImage = sys.argv[1]
image = Image.open(inputImage, 'r')
pixels = list(image.getData())

pixelData = open("pixelData", 'w')
for pixel in pixels:
	pixelData.write(pixel)
pixelData.close()