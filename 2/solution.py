def containsExactlyN(sequence, N):
    for letter in sequence:
        if sequence.count(letter) == N:
            return True
    
    return False


inputFile = open('input', 'r')
inputIDs = inputFile.readlines()
inputFile.close()

exactlyTwoCount = 0
exactlyThreeCount = 0

for line in inputIDs:
    if containsExactlyN(line, 2):
        exactlyTwoCount += 1

    if containsExactlyN(line, 3):
        exactlyThreeCount += 1

print(exactlyTwoCount * exactlyThreeCount)
