import shelve
shelfFile = shelve.open("mydata")
cats = ["Trixie", "Charlie", "Toby"]
shelfFile["cats"] = cats
shelfFile.close()