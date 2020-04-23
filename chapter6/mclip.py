#! python3
#mclip.py - A multi-clipboard program
import sys, pyperclip

TEXT = {"Agree": """Yes, I agree. That sounds find to me.""",
		"Busy:": """Sorry, can we do this later this week or next week?""",
		"Upsell": """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
	print("Usage: python mclip.py [keyphrase] - copy phrase text")
	sys.exit()

keyphrase = sys.argv[1] #first commandline arg is the keyphrase

if keyphrase in TEXT:
	pyperclip.copy(TEXT[keyphrase])
	print("Text for " + keyphrase + " copied to clipboard.")
else:
	print("There is no text for " + keyphrase)