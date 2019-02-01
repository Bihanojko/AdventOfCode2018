letterAIdx = len('Step ')
letterBIdx = len('Step X must be finished before step ')

inputFile = open('input', 'r')
instructions = inputFile.readlines()
inputFile.close()

prerequisites = {}

for dependency in instructions:
    if dependency[letterBIdx] not in prerequisites:
        prerequisites[dependency[letterBIdx]] = [dependency[letterAIdx]]
    else:
        prerequisites[dependency[letterBIdx]] += dependency[letterAIdx]

    if dependency[letterAIdx] not in prerequisites:
        prerequisites[dependency[letterAIdx]] = []


workersFree = 5
seconds = 0
jobWillBeDone = []

while True:
    while seconds in [x[0] for x in jobWillBeDone]:
        workersFree += 1
        finishedStep = [x for x in jobWillBeDone if x[0] == seconds][0]
        jobWillBeDone = [x for x in jobWillBeDone if x != finishedStep]
        for key in prerequisites:
            prerequisites[key] = [x for x in prerequisites[key] if x != finishedStep[1]]

    availableSteps = sorted([step for step in prerequisites.keys() if prerequisites[step] == []])

    while availableSteps != [] and workersFree > 0:
        step = availableSteps[0]
        workersFree -= 1
        jobWillBeDone.append([seconds + ord(step) - ord('A') + 60 + 1, step])
        del availableSteps[0]
        del prerequisites[step]
    
    if len(prerequisites) == 0 and workersFree == 5:
        break
    
    seconds += 1

print(seconds)
