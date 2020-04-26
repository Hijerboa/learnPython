import pyinputplus as pyip
import time, random

numTotalGames = 10
numGamesWon = 0

for game in range(10):
    num1 = random.randint(0, 9)
    num2 = random.randint(0, 9)
    prompt = "#%s: %s x %s = " % (game, num1, num2)
    try:
        pyip.inputStr(prompt, allowRegexes=["^%s$" % (num1 * num2)],
                                            blockRegexes = [(".*", "Incorrect!")],
                                            timeout=8, limit=3)
    except pyip.TimeoutException:
            print("Out of Time!")
    except pyip.RetryLimitException:
            print("Out of tries!")
    else:
            print("Correct!")
            numGamesWon += 1
    time.sleep(1)
print("Score: %s / %s" % (numGamesWon, numTotalGames))