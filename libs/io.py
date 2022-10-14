
from PIL import Image
import io

def SaveImageData(bytes : bytes, filepath=None, quality=100, optimize=True):
	return Image.open(io.BytesIO(bytes)).save(filepath, quality=quality, optimize=optimize)
	#return Image.open(bytes).save(filepath, quality=quality, optimize=optimize)
