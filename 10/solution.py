import re


def splitAndTransform(description):
    return [int(description[1 : description.find(',')]), int(description[description.find(',') + 1 : -1])]


def processInputFile(inputContent):
    pointCoordinates = []
    pointVelocities = []

    for point in inputContent:
        descriptions = re.findall(r'<[^>]*>', point)

        pointCoordinates.append(splitAndTransform(descriptions[0]))
        pointVelocities.append(splitAndTransform(descriptions[1]))
    
    return pointCoordinates, pointVelocities


def movePoints():
    global pointCoordinates

    for i in range(pointCount):
        pointCoordinates[i] = [pointCoordinates[i][0] + pointVelocities[i][0], pointCoordinates[i][1] + pointVelocities[i][1]]


def printMessage():
    maxX = max(pointCoordinates, key = lambda x : x[0])[0]
    minX = min(pointCoordinates, key = lambda x : x[0])[0]
    maxY = max(pointCoordinates, key = lambda x : x[1])[1]
    minY = min(pointCoordinates, key = lambda x : x[1])[1]

    for y in range(minY, maxY + 1):
        for x in range(minX, maxX + 1):
            if [x, y] in pointCoordinates:
                print('#', end='')
            else:
                print('.', end='')

        print('')


inputFile = open('input', 'r')
inputContent = inputFile.readlines()
inputFile.close()

pointCoordinates, pointVelocities = processInputFile(inputContent)

pointCount = len(pointCoordinates)

for i in range(10076):
    movePoints()

printMessage()
