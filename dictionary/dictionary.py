# Import json library
import json

# Import library for 'Text Pricessing Serveices'
from difflib import get_close_matches as gcmatch

# Load json data as dictionary
data = json.load(open("data.json"))

# Function for definition
def definition(word):

	# Remov in lower case
	word = word.lower()

	# Check existing
	if word in data:
		return data[word]
	# Word start with capital letter
	elif word.title() in data:
		return data[word.title()]
	# The acronimus
	elif word.upper() in data:
		return data[word.upper()]
	# Finding the maximum match wit user unput and data
	elif len(gcmatch(word, data.keys())) > 0:
		action = input("Maybe you mean %s [y/n]: " % gcmatch(word, data.keys())[0])

		if (action.lower() == "y") or (action.lower() == "yes"):
			return data[gcmatch(word, data.keys())[0]]
		elif (action.lower() == "n") or (action.lower() == "no"):
			return ("The word does not exist in dictionary")
		else:
			return ("Sorry! I don't understand you")
			

# Insert from user
user_word = input("Enter your word: ")

# String or list string in output
output = definition(user_word)

# List string sepsrsted and output one by one
if type(output) == list:
	for i in output:
		print("-", i)

# One line just output
else:
	print("-", output)
