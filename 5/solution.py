import re

inputFile = open('input', 'r')
inputPolymer = inputFile.read().strip()
inputFile.close()

polarityDifference = ord('a') - ord('A')

reactedPolymer = inputPolymer

while True:
    inputPolymer = reactedPolymer

    for char in range(ord('A'), ord('Z') + 1):
        reactedPolymer = re.sub(r'(' + chr(char) + chr(char + polarityDifference) + r'|' + chr(char + polarityDifference) + chr(char) + r')', '', reactedPolymer)
    
    if len(reactedPolymer) == len(inputPolymer):
        break

print(len(reactedPolymer))
