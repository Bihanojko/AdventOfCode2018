inputFile = open('input', 'r')
inputSequence = inputFile.readlines()
inputFile.close()

frequency = 0
reachedFrequencies = []

freqChangesIndex = 0
freqChangesLength = len(inputSequence)

while(frequency not in reachedFrequencies):
    reachedFrequencies.append(frequency)
    difference = int(inputSequence[freqChangesIndex % freqChangesLength][1:-1])
    frequency += difference if inputSequence[freqChangesIndex % freqChangesLength][0] == '+' else difference * (-1)
    freqChangesIndex += 1

print(frequency)
