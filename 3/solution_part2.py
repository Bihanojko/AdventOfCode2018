def splitLine(line):
    xStart = int(line[line.find('@') + 2 : line.find(',')])
    yStart = int(line[line.find(',') + 1 : line.find(':')])
    xLength = int(line[line.find(':') + 2 : line.find('x')])
    ylength = int(line[line.find('x') + 1 : line.find('\n')])

    return xStart, yStart, xLength, ylength


def overlaps(line):
    xStart, yStart, xLength, ylength = splitLine(line)
    
    for i in range(xStart, xStart + xLength):
        for j in range(yStart, yStart + ylength):
            key = str(i) + "," + str(j) 

            if claimedAreas[key] > 1:
                return True

    return False



inputFile = open('input', 'r')
inputClaims = inputFile.readlines()
inputFile.close()

claimedAreas = {}

for line in inputClaims:
    xStart, yStart, xLength, ylength = splitLine(line)

    for i in range(xStart, xStart + xLength):
        for j in range(yStart, yStart + ylength):
            key = str(i) + "," + str(j) 

            if key not in claimedAreas:
                claimedAreas[key] = 1
            else:
                claimedAreas[key] = claimedAreas[key] + 1


for line in inputClaims:
    if not overlaps(line):
        print(line[1 : line.find('@') - 1])
        exit(0)
