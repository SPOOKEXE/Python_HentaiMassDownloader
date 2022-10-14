from bs4 import BeautifulSoup
from urllib.request import urlopen

from libs import scrape, io, thread

import time, os

DIRECTORY_PATH = "."
SCRAPE_WORKER_COUNT = 25

# Scrape the page and download the images
def SCRAPE_PAGE(page_url):
	global DIRECTORY_PATH
	for url in scrape.ScrapeMedia(page_url):
		# print(page_url)
		scrape.DownloadImageMedia(url, DIRECTORY_PATH)

# Website Scanning
from http.client import HTTPResponse
def FORMAT_1_SCRAPE(base_url, argument):
	response : HTTPResponse = urlopen(argument)
	# print(response.status, argument)
	soup = BeautifulSoup(response, "html.parser")
	page_urls = []
	for link in soup.findAll('a'):
		href = link.get('href')
		if href != None and href.find("/post/show/") != -1:
			page_urls.append(base_url + href)
	thread.CompleteThreadTask(SCRAPE_PAGE, page_urls, worker_count=SCRAPE_WORKER_COUNT)

def KONACHAN_SITE(argument):
	print("KONACHAN - ", argument)
	return FORMAT_1_SCRAPE("https://konachan.com", argument)

def YANDERE_SITE(argument):
	print("YANDERE - ", argument)
	return FORMAT_1_SCRAPE("https://yande.re", argument)

def DANBOORU_SITE(argument):
	print("DANBOORU - ", argument)
	return FORMAT_1_SCRAPE("https://danbooru.donmai.us", argument)

# Website URL Constructors
def FORMAT_1_GEN(baseURL : str, total_pages : int, tag_list : list[str]) -> list[str]:
	url_array = []
	tag_list = "+".join(tag_list)
	for page_number in range(total_pages):
		url_array.append(str.format(baseURL + "/post?page={}&tags={}", page_number, tag_list))
	return url_array

def KONACHAN_URL_GEN(total_pages : int, tag_list : list[str]) -> list[str]:
	return FORMAT_1_GEN("https://konachan.com", total_pages, tag_list)

def YANDERE_URL_GEN(total_pages : int, tag_list : list[str]) -> list[str]:
	return FORMAT_1_GEN("https://yande.re", total_pages, tag_list)

def DANBOORU_URL_GEN(total_pages : int, tag_list : list[str]) -> list[str]:
	return FORMAT_1_GEN("https://danbooru.donmai.us", total_pages, tag_list)

URL_GEN_TO_SITE_PARSE = {}
URL_GEN_TO_SITE_PARSE[KONACHAN_URL_GEN] = KONACHAN_SITE
URL_GEN_TO_SITE_PARSE[YANDERE_URL_GEN] = YANDERE_SITE
URL_GEN_TO_SITE_PARSE[DANBOORU_URL_GEN] = DANBOORU_SITE

# FOR DEBUG
def WriteOutDebugInfo(urls_dict : dict, filename="output.json") -> None:
	try:
		os.remove(filename)
	except:
		pass
	with open(filename, "w") as file:
		lines = []
		for FUNC in urls_dict:
			lines.append(str(FUNC))
			for page_n_list in urls_dict[FUNC]:
				for url_v in page_n_list:
					lines.append("\t" + url_v)
		file.write("\n".join(lines))
