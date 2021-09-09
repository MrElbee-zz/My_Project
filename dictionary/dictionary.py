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
		# If user know what want	
		elif (action.lower() == "n") or (action.lower() == "no"):

			action = input("The word does not exist in dictionary. Do you want to add word %s in dictionary? [y/n]: " % user_word)
			
			# Add new word and definition in json file
			if (action.lower() == "y") or (action.lower() == "yes"):
				definition_new_word = input("What that word mean? : ")

				with open('data.json', 'w') as f:

					# Add word in variadle 
					data[user_word] = [definition_new_word]
					
					# Rewrite file
					f.write(json.dumps(data))


				return data[user_word]

			# In any incomprehensible situation, I apologize.
			elif (action.lower() == "n") or (action.lower() == "no"):
				return ("Sorry! I don't know that word")
			else:
				return ("Sorry! I don't understand you")
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
