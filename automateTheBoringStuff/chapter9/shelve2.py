import shelve
shelfFile = shelve.open("mydata")
print(type(shelfFile))
print(shelfFile["cats"])
shelfFile.close()
