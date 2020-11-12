#!/usr/bin/python

def vowelCount():
	vowels = "aeiuo"
	user_string = input("Enter a sentence or a word: ")
	results = dict()
	
	for chars in set(user_string.lower()):
		if chars in vowels:
			results[chars] = list(user_string.lower()).count(chars)
	print(results)

vowelCount()
