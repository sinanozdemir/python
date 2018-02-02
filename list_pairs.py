#!/usr/bin/python

def listPairs(x,y):
	pairs = dict()
	hold = []
	count = 0

	for i in x:
		hold.append(i)
		if sum(hold) == y:
			count += 1
			pairs.setdefault(count, []).extend(hold)
			hold[:] = []

	print pairs

listPairs([1,3,2,5,1],6)


