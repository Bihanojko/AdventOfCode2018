def getNearestLocation(x, y):
    minDistance = gridMaxX + gridMaxY
    minDistanceLocationID = -1
    border = False

    for idx, location in enumerate(inputCoordinates):
        distance = abs(x - location[0]) + abs(y - location[1])

        if distance < minDistance:
            minDistance = distance
            minDistanceLocationID = idx
            border = False
        
        elif distance == minDistance:
            border = True
        
    if border:
        return -1
    else:
        return minDistanceLocationID


def finite(idx):
    borders = nearestLocations[0] + nearestLocations[-1] + [row[0] for row in nearestLocations] + [row[-1] for row in nearestLocations]

    if idx in borders:
        return False
    else:
        return True


inputFile = open('input', 'r')
inputCoordinates = inputFile.readlines()
inputFile.close()

inputCoordinates = [[int(x[: x.find(',')]), int(x[x.find(',') + 2 : x.find('\n')])] for x in inputCoordinates]

gridMaxX = max(inputCoordinates, key = lambda x: x[0])[0]
gridMaxY = max(inputCoordinates, key = lambda x: x[1])[1]

nearestLocations = []


for y in range(gridMaxY + 1):
    row = []

    for x in range(gridMaxX + 1):
        row.append(getNearestLocation(x, y))

    nearestLocations.append(row)

largestArea = -1

for idx, location in enumerate(inputCoordinates):
    if finite(idx):
        areaSize = sum([row.count(idx) for row in nearestLocations])
        if areaSize > largestArea:
            largestArea = areaSize

print(largestArea)
