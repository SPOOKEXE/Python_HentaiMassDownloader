
import os
from libs import thread, utility, websites

THREAD_COUNT = 10

# ============================================================
websites.DIRECTORY_PATH = utility.AskForStoreDirectory(parent_spec_file=__file__)

# ============================================================
total_pages : int = utility.GetInputOfType("How many pages are to be searched? ", int)
search_tags : list = []
while True:
	os.system('cls||clear')
	print("Enter tags you would like to search for (put 'done' when finished, 'del' to remove previous). ")
	print("Current Tags: \n\t " + str(search_tags) + "\n")
	input_tag : str = input("")
	if input_tag == 'done':
		break
	elif input_tag == 'del':
		search_tags.pop()
	else:
		search_tags.append(input_tag)
os.system('cls||clear')

# ============================================================
print("Removing singular tag values from tag array.")
search_tags = utility.PowerSet(search_tags)
if len(search_tags) > 1: # if there is more than 1 tag
	utility.FilterMinListCountFromList(search_tags, minimum_length=2)

# ============================================================
print("Resolving URLs")
urls = {}
for URL_GEN in websites.URL_GEN_TO_SITE_PARSE:
	SITE_PARSE_FUNC = websites.URL_GEN_TO_SITE_PARSE[URL_GEN]

	if urls.get(SITE_PARSE_FUNC) == None:
		urls[SITE_PARSE_FUNC] = []

	for power_set in search_tags:
		urls[SITE_PARSE_FUNC].append( URL_GEN(total_pages, power_set) )

websites.WriteOutDebugInfo(urls, filename="output.json")

# ============================================================
print("Searching ", total_pages, " pages.", "\n Tags: ", search_tags)
print("Starting Scanning & Download Threads")
def Parse(PARSER):
	for arguments in urls.get(PARSER):
		print("==========================================================")
		print(PARSER, arguments)
		thread.CompleteThreadTask(parent_function=PARSER, arguments_array=arguments, worker_count=THREAD_COUNT)

DICT_INDEXES = []
for PARSER in urls:
	DICT_INDEXES.append(PARSER)
thread.CompleteThreadTask(parent_function=Parse, arguments_array=DICT_INDEXES, worker_count=THREAD_COUNT)

print("Finished")