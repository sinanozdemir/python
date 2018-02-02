#!/usr/bin/python

def anagram():
	string_1 = input("Enter first sentence: ")
	string_2 = input("Enter second sentence: ")
	
	new_string_1 = ''.join([i for i in sorted(string_1) if i != ' '])
	new_string_2 = ''.join([i for i in sorted(string_2) if i != ' '])

	if new_string_1 == new_string_2:
		print "True"
	else:
		print "False"

anagram()
