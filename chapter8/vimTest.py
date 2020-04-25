import pyinputplus as pyip
print("Please enter your age")
age = pyip.inputNum()
if age < 18:
    print("Bro you're not 18 yet get out")
else:
    print("yay you're an adult!")
    print("What's your name?")
    name = pyip.inputStr()
    print("Hi there " + name + "! Now get out!")
