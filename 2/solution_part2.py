def differInOneChar(sequence1, sequence2):
    diffCount = 0

    for idx in range(len(sequence1)):
        if sequence1[idx] != sequence2[idx]:
            diffCount += 1
    
    return diffCount == 1


inputFile = open('input', 'r')
inputIDs = inputFile.readlines()
inputFile.close()

for line in inputIDs:
    for line2 in inputIDs:
        if line == line2:
            continue
        
        if differInOneChar(line, line2):
            print(''.join([x for idx, x in enumerate(line) if line[idx] == line2[idx]]))
            exit(0)
