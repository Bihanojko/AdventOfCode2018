HEADER_LENGTH = 2
entriesSum = 0

inputFile = open('input', 'r')
inputSequence = inputFile.readlines()
inputFile.close()

inputSequence = inputSequence[0].split(' ')


def addEntries(metadataEntries):
    global entriesSum

    metadataEntries = [int(x) for x in metadataEntries]
    entriesSum += sum(metadataEntries)



def processChildSequences(childNodesCount):
    global inputSequence

    for _ in range(childNodesCount):
        childSubnodesCount = int(inputSequence[0])
        entriesCount = int(inputSequence[1])

        if childSubnodesCount == 0:
            metadataEntries = inputSequence[HEADER_LENGTH : HEADER_LENGTH + entriesCount]
            addEntries(metadataEntries)
            inputSequence = inputSequence[entriesCount + HEADER_LENGTH :]

        else:
            inputSequence = inputSequence[2 :]
            processChildSequences(childSubnodesCount)

            metadataEntries = inputSequence[: entriesCount]
            addEntries(metadataEntries)
            inputSequence = inputSequence[entriesCount :]



def processNode():
    global entriesSum
    global inputSequence

    childNodesCount = int(inputSequence[0])
    entriesCount = int(inputSequence[1])
    metadataEntries = inputSequence[-entriesCount :]
    addEntries(metadataEntries)

    inputSequence = inputSequence[2 : -entriesCount]

    processChildSequences(childNodesCount)



processNode()

print(entriesSum)
