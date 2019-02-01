inputFile = open('input', 'r')
inputSequence = inputFile.readlines()
inputFile.close()

frequency = 0

for line in inputSequence:
    difference = int(line[1:-1])
    frequency += difference if line[0] == '+' else difference * (-1)

print(frequency)
