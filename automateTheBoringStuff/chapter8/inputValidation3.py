import pyinputplus as pyip

response = pyip.inputNum(blockRegexes=[r'[02468]$'])
print(response)
