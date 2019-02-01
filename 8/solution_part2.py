HEADER_LENGTH = 2
rootNodeValue = 0

inputFile = open('input_min', 'r')
# inputFile = open('input', 'r')
inputSequence = inputFile.readlines()
inputFile.close()

inputSequence = inputSequence[0].split(' ')


def addEntries(metadataEntries):
    global rootNodeValue

    metadataEntries = [int(x) for x in metadataEntries]
    # rootNodeValue += sum(metadataEntries)
    return sum(metadataEntries)


def processChildSequences(childNodesCount):
    global inputSequence

    childNodeValues = []

    for _ in range(childNodesCount):
        childSubnodesCount = int(inputSequence[0])
        entriesCount = int(inputSequence[1])

        if childSubnodesCount == 0:
            metadataEntries = inputSequence[HEADER_LENGTH : HEADER_LENGTH + entriesCount]
            childNodeValues.append(addEntries(metadataEntries))
            inputSequence = inputSequence[entriesCount + HEADER_LENGTH :]

        else:
            inputSequence = inputSequence[2 :]
            processChildSequences(childSubnodesCount)

            metadataEntries = inputSequence[: entriesCount]
            # addEntries(metadataEntries)
            # TODO
            inputSequence = inputSequence[entriesCount :]



def processNode():
    global rootNodeValue
    global inputSequence

    childNodesCount = int(inputSequence[0])
    entriesCount = int(inputSequence[1])
    metadataEntries = inputSequence[-entriesCount :]

    for entry in metadataEntries:
        print(entry)
        if entry < childNodesCount:
            

    inputSequence = inputSequence[2 : -entriesCount]

    # processChildSequences(childNodesCount)



processNode()

print(rootNodeValue)
