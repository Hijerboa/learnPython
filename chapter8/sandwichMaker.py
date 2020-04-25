import pyinputplus as pyip

price = 0
breads = ["Wheat", "White", "Sourdough"]
meats = ["Chicken", "Turkey", "Ham", "Tofu"]
cheeses = ["Cheddar", "Swiss", "Mozzarella"]
toppings = ["Mayo", "Mustard", "Lettuce", "Tomato"]
print("Welcome to the Sandwich Shoppe... What can I get you?")
bread = pyip.inputMenu(breads)
if bread == "Sourdough":
    price += 1.25
else:
    price += 1
meat = pyip.inputMenu(meats)
if meat == "Tofu":
    price += 3
else:
    price += 2.5
cheese = pyip.inputYesNo("Do you want cheese?\n")
if cheese == "yes":
    price += 0.5
    print("What type of cheese do you want?")
    cheeseType = pyip.inputMenu(cheeses)
for topping in toppings:
    prompt = "Do you want " + topping + "?\n"
    answer = pyip.inputYesNo(prompt)
    if answer == "yes":
        price += 0.25
prompt = "How many of these bad bois do you want?\n"
numSand = pyip.inputNum(prompt, min = 1)
totalPrice = price * numSand
print("Okay now give me " + str(totalPrice) + " Dollary Doos")
