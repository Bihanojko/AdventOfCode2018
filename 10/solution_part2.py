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


inputFile = open('input', 'r')
inputContent = inputFile.readlines()
inputFile.close()

pointCoordinates, pointVelocities = processInputFile(inputContent)

pointCount = len(pointCoordinates)

for i in range(10076):
    movePoints()

print(i + 1)
