
from requests import get as requests_get
from bs4 import BeautifulSoup
from urllib.request import urlopen

from libs.io import SaveImageData

DEFAULT_MEDIA_TYPE_WHITELIST = [".png", ".jpg", ".webp"]

# Download an Image file
def DownloadImageMedia( MediaURL : str, filepath=None ) -> None:
	response = requests_get(MediaURL)
	filename = MediaURL[MediaURL.rfind("/")+1:len(MediaURL)]
	if filename.find(".") == -1: # if no extension, add one
		filename = filename + ".png"
	if filepath == None:
		filepath = "."
	full_path = filepath + "/" + filename
	print(full_path)
	SaveImageData(response.content, filepath=full_path, quality=80, optimize=True)
	# with open(full_path, "wb") as file:
	# 	file.write(response.content)

# Check if its a valid image
def IsURLAnImage(URL : str, whitelist=DEFAULT_MEDIA_TYPE_WHITELIST) -> bool:
	for endExtension in whitelist:
		if URL.find(endExtension) != -1:
			return True
	return False

# Returns a list of urls that point to the direct image data
def ScrapeMedia(url : str) -> list[str]:
	media_urls = []
	soup = BeautifulSoup(urlopen(url), "html.parser")
	for link in soup.findAll('a'):
		href : str = link.get('href')
		if href != None and IsURLAnImage(href, whitelist=DEFAULT_MEDIA_TYPE_WHITELIST):
			media_urls.append(href)
	return media_urls
