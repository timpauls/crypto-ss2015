from datetime import datetime

startTime = datetime.now()

def xorStrings(string1, string2):
	return "".join(map(lambda a: chr(ord(a[0])^ord(a[1])), zip(string1, string2)))

firstCypher = "c268325cd2c38573".decode("hex")
secondcypher = "c563235ddecc877d".decode("hex")

xoredWords = xorStrings(firstCypher, secondcypher)

with open("8_letter_words.txt") as file:
	wordlist = file.read().splitlines();

for word in wordlist:
	decrypted = xorStrings(xoredWords, word)
	if decrypted in wordlist:
		print "The words are '%s' and '%s'"%(decrypted, word)
		break;

print datetime.now() - startTime