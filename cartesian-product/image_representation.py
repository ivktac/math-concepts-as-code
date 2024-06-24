from PIL import Image
import itertools

width = 500
height = 300

image = Image.new("RGB", (width, height))

pixels = image.load()

for x, y in itertools.product(range(width), range(height)):
	pixels[x, y] = (255, 0, 0)

image.show()
