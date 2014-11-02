candyFile = open("candy.txt", "r")

candyDict = {}
totalCandyCount = 0

for line in candyFile:
    totalCandyCount += 1
    pieceOfCandy = line.strip("\n")

    if pieceOfCandy in candyDict:
        candyDict[pieceOfCandy] += 1
    else:
        candyDict[pieceOfCandy] = 1

for key, value in candyDict.items():
    candy = key + "(" + str(value) + "):"

    while len(candy) < 25:
        candy = " " + candy

    print(candy, "I" * value, " {:.1%}".format(value/totalCandyCount),
        sep="")

print("\n", "Total pieces of candy: ", totalCandyCount, sep="")
