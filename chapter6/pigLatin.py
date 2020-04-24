#English to Pig Latin

print("Enter the english language you wish to have translated into Pig Latin:")

english = input()
words = english.split(" ")
VOWELS = ("a", "e", "i", "o", "u", "y")

for i in range(len(words)):
	word = words[i]
	if word.isalpha() == True:
		isTitle = word.istitle()
		isUpper = word.isupper()
		word = word.lower()
		if word[0] in VOWELS:
			word = word + "yay"
		else:
			for letter in range(len(word)):
				if word[letter] in VOWELS:
					firstVowel = letter
					break
			tupledString = word.partition(word[firstVowel])
			word = tupledString[1] + tupledString[2] + tupledString[0] + "ay"
		if isTitle:
			word = word.title()
		if isUpper:
			word = word.upper()
	words[i] = word


finalString = " ".join(words)
print(finalString)