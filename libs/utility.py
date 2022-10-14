import os

# Ask user for the storage directory
def AskForStoreDirectory() -> str:
	os.system('cls||clear')
	directory = '/'.join(__file__.split("\\")[0:-1]) + "/" + input("Enter the container name. ")
	try: 
		os.makedirs(directory)
	except:
		pass
	os.chdir(directory)
	return directory

# Get the powerset of the items (every combination of the items)
def PowerSet(items : list) -> list[list]:
	N = len(items)
	combinations = []
	for i in range(2**N):
		combo = []
		for j in range(N):
			if (i >> j) % 2 == 1:
				combo.append(items[j])
		combinations.append(combo)
	return combinations

# Remove lists in a list that are smaller than a length
def FilterMinListCountFromList(parent_list : list, minimum_length=2):
	index = 0
	while index < len(parent_list):
		array = parent_list[index]
		if len(array) < minimum_length: # remove any singlular tags
			parent_list.pop(index)
		else:
			index += 1

# Get user input of a specific type
def GetInputOfType(prompt_text : str, inputType : type) -> type:
	value : int = None
	while (value==None):
		inp : str = input(prompt_text)
		try:
			value = inputType(inp)
		except:
			print("Passed input does not match the type ", inputType)
			pass
	return value


