UPPER_LIMIT = 26

def affineCaesar(a, b, p):
	return (a*p+b) % UPPER_LIMIT

def debugPrint(a, b):
	results = []
	for p in range(UPPER_LIMIT):
		cypher = affineCaesar(a, b, p)
		#print "E([%d, %d], %d) = %d"%(a, b, p, cypher)
		if cypher in results:
			print "[%d, %d]: not one-to-one: %d is dupicate"%(a, b, p)
			break;
		else:
			#print "adding %d to results"%cypher
			results.append(cypher)

def isOneToOne(a, b):
	results = []
	for p in range(UPPER_LIMIT):
		cypher = affineCaesar(a, b, p)
		if cypher in results:
			return False
		else:
			results.append(cypher)
	return True


def printAllOneToOne():
	for a in range(UPPER_LIMIT):
		if (isOneToOne(a, 3)):
			print "a = %d"%a

def countAllOneToOne():
	count = 0
	for a in range(UPPER_LIMIT):
		for b in range(UPPER_LIMIT):
			if isOneToOne(a, b):
				count += 1
	return count;

print countAllOneToOne()