
import time

# Website Scanning
def KONACHAN_SITE(argument):
	print("KONACHAN - ", argument)
	time.sleep(3)

def YANDERE_SITE(argument):
	print("YANDERE - ", argument)
	time.sleep(3)

def DANBOORU_SITE(argument):
	print("DANBOORU - ", argument)
	time.sleep(3)

def GELBOORU_SITE(argument):
	print("GELBOORU - ", argument)
	time.sleep(3)

# Website URL Constructors
def FORMAT_1_GEN(baseURL : str, total_pages : int, tag_list : list[str]) -> list[str]:
	url_array = []
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
URL_GEN_TO_SITE_PARSE[YANDERE_URL_GEN] = DANBOORU_SITE
URL_GEN_TO_SITE_PARSE[DANBOORU_URL_GEN] = GELBOORU_SITE

# FOR DEBUG
import os
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
