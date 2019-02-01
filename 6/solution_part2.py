def getDistancesSum(x, y):
    distancesSum = 0

    for location in inputCoordinates:
        distancesSum += abs(x - location[0]) + abs(y - location[1])

    return 1 if distancesSum < 10000 else 0


inputFile = open('input', 'r')
inputCoordinates = inputFile.readlines()
inputFile.close()

inputCoordinates = [[int(x[: x.find(',')]), int(x[x.find(',') + 2 : x.find('\n')])] for x in inputCoordinates]


gridMaxX = max(inputCoordinates, key = lambda x: x[0])[0]
gridMaxY = max(inputCoordinates, key = lambda x: x[1])[1]

safeDistances = []


for y in range(gridMaxY + 1):
    row = []

    for x in range(gridMaxX + 1):
        row.append(getDistancesSum(x, y))

    safeDistances.append(row)


print(sum([sum(row) for row in safeDistances]))
