import re


polarityDifference = ord('a') - ord('A')


def collapsePolymer(inputPolymer):
    reactedPolymer = inputPolymer

    while True:
        inputPolymer = reactedPolymer

        for char in range(ord('A'), ord('Z') + 1):
            reactedPolymer = re.sub(r'(' + chr(char) + chr(char + polarityDifference) + r'|' + chr(char + polarityDifference) + chr(char) + r')', '', reactedPolymer)
        
        if len(reactedPolymer) == len(inputPolymer):
            break

    return reactedPolymer


inputFile = open('input', 'r')
inputPolymer = inputFile.read().strip()
inputFile.close()


minimumLength = len(inputPolymer)

for char in range(ord('A'), ord('Z') + 1):
    reducedPolymer = re.sub(r'(' + chr(char) + r'|' + chr(char + polarityDifference) + r')', '', inputPolymer)
    collapsedPolymerLength = len(collapsePolymer(reducedPolymer))

    if collapsedPolymerLength < minimumLength:
        minimumLength = collapsedPolymerLength

print(minimumLength)
