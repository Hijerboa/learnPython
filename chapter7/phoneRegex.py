#! python3
#Finds emails and phone numbers in the clip board

import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))? # area code
	(\s|-|\.)? # separator
	(\d{3}) # first 3 digits
	(\s|-|\.) # separator
	(\d{4}) # last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))? # extension
	)''', re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
 [a-zA-Z0-9._%+-]+ # username
 @ # @ symbol
 [a-zA-Z0-9.-]+ # domain name
	(\.[a-zA-Z]{2,4}) # dot-something
	)''', re.VERBOSE)

#Find all matches in the clipboard text
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]]) #join the separated parts of the phone numbers
	if groups[8] != "": #if there is an extension, add it
		phoneNum += " x" + groups[8]
	matches.append(phoneNum)
for groups in emailRegex.findall(text):
	matches.append(groups[0])

if len(matches) > 0:
	pyperclip.copy("\n".join(matches))
	print("Copied clipboard:")
	print("\n".join(matches))
else:
	print("No phone numbers or email addresses found")