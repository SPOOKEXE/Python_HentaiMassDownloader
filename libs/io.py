
from PIL import Image

def SaveImageData(bytes : bytes, filepath=None, quality=100, optimize=True):
	return Image.Image(bytes).save(filepath, quality=quality, optimize=optimize)
