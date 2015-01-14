
# -*- coding: utf-8 -*-

allowed_words = (
	{
		"type": "direction",
		"words": ("north", "south", "east", "west", "down", "up", "left", "right", "back")
	},
	{
		"type": "verb",
		"words": ("go", "stop", "kill", "eat")
	},
	{
		"type": "stop",
		"words": ("the", "in", "of", "from", "at", "it")
	},
	{
		"type": "noun",
		"words": ("door", "bear", "princess", "cabinet")
	}
	# numbers are checked programatically
)

def scan(text_input):
	words = text_input.split()
	sentence = []
	count = 0

	for word in words:
		# first test if it is a number
		number = toNumber(word)

		if number is not None:
			sentence.append(("number", number))
		else:
			# else test for the other types
			count = 0
			for entry in allowed_words:
				if word in entry["words"]:
					sentence.append((entry["type"], word))
					break;
				count += 1

			if count is len(allowed_words):
				sentence.append(("error", word))

	return sentence

def toNumber(word):
	try:
		return int(word)
	except ValueError:
		return None


if __name__ == "__main__":
    print scan("north south east")
    print scan("go kill eat")
    print scan("the in of")
    print scan("bear princess")
    print scan("3 91234")
    print scan("bear IAS princess")
