
from requests import get as requests_get
from bs4 import BeautifulSoup
from urllib import request as urllib_request

from libs.io import SaveImageData

DEFAULT_MEDIA_TYPE_WHITELIST = [".png", ".jpg", ".webp"]

# Download an Image file
def DownloadImageMedia( MediaURL : str ) -> None:
	response = requests_get(MediaURL)
	filename = MediaURL[MediaURL.rfind("/")+1:len(MediaURL)]
	if filename.find(".") == -1: # if no extension, add one
		filename = filename + ".png"
	SaveImageData(response.content, quality=80, optimize=True)

# Check if its a valid image
def IsURLAnImage(URL : str, whitelist=DEFAULT_MEDIA_TYPE_WHITELIST) -> bool:
	for endExtension in whitelist:
		if URL.find(endExtension) != -1:
			return True
	return False

# Returns a list of urls that point to the direct image data
def ScrapeMedia(url : str) -> list[str]:
	media_urls = []
	soup = BeautifulSoup(urllib_request.request.urlopen(url), "html.parser")
	for link in soup.findAll('a'):
		href : str = link.get('href')
		if href != None and IsURLAnImage(href, whitelist=DEFAULT_MEDIA_TYPE_WHITELIST):
			media_urls.append(href)
	return media_urls
