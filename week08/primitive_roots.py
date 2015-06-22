#!/usr/bin/python

N = 53
primitive_roots = []

for prospect in xrange(1, N):
	numbers = []
	isValid = True
	for i in xrange(1, N):
		number = (prospect**i) % N
		if number in numbers:
			isValid = False
			break;
		else:
			numbers.append(number)

	if isValid:
		primitive_roots.append(prospect)

print primitive_roots