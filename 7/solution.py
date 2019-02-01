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

while len(prerequisites) != 0:
    availableSteps = sorted([step for step in prerequisites.keys() if prerequisites[step] == []])
    step = availableSteps[0]

    print(step, end='')
    del prerequisites[step]
    
    for key in prerequisites:
        prerequisites[key] = [x for x in prerequisites[key] if x != step]
