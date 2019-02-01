import re
import datetime
import operator


def orderRecords(inputRecords):
    return sorted(inputRecords)


def parseRecord(record):
    timestamp = record[record.find('[') + 1 : record.find(']')]
    event = record[record.find(']') + 2 : record.find('\n')]

    return timestamp, event 


def getGuardID(event):
    return re.search(r'#\d+', event).group(0)[1:]


def minutesAsleep(asleepTimestamp, wakeTimestamp):
    asleepDate = datetime.datetime.strptime(asleepTimestamp, '%Y-%m-%d %H:%M')
    wakeDate = datetime.datetime.strptime(wakeTimestamp, '%Y-%m-%d %H:%M')

    asleep = []
    minuteAsleep = asleepDate

    while(minuteAsleep != wakeDate):
        asleep.append(minuteAsleep.minute)
        minuteAsleep += datetime.timedelta(minutes = +1)

    return asleep


def getGuardsAsleepMinutes(orderedRecords):
    guardOnShift = -1
    guardsAsleep = {}
    asleepTimestamp = ''

    for record in orderedRecords:
        timestamp, event = parseRecord(record)

        if 'begins shift' in event:
            guardOnShift = getGuardID(event)

        elif 'falls asleep' in event:
            asleepTimestamp = timestamp

        elif 'wakes up' in event:
            if guardOnShift not in guardsAsleep:
                guardsAsleep[guardOnShift] = minutesAsleep(asleepTimestamp, timestamp)
            else:
                guardsAsleep[guardOnShift] += minutesAsleep(asleepTimestamp, timestamp)

            asleepTimestamp = ''
        
    return guardsAsleep


def getFrequentlyAsleepGuard(guardsAsleep):
    guardFrequentlyAsleepID = -1
    guardFrequentlyAsleepMinute = -1
    maximumSleepFrequency = -1
  
    for guardID in guardsAsleep:
        guardMostAsleepMinute = max(set(guardsAsleep[guardID]), key=guardsAsleep[guardID].count)

        if maximumSleepFrequency < guardsAsleep[guardID].count(guardMostAsleepMinute):
            guardFrequentlyAsleepMinute = guardMostAsleepMinute
            maximumSleepFrequency = guardsAsleep[guardID].count(guardMostAsleepMinute)
            guardFrequentlyAsleepID = guardID

    return int(guardFrequentlyAsleepID) * guardFrequentlyAsleepMinute


inputFile = open('input', 'r')
inputRecords = inputFile.readlines()
inputFile.close()


orderedRecords = orderRecords(inputRecords)

guardOnShift = -1
guardsAsleep = {}
asleepTimestamp = ''


for record in orderedRecords:
    timestamp, event = parseRecord(record)

    if 'begins shift' in event:
        guardOnShift = getGuardID(event)

    elif 'falls asleep' in event:
        asleepTimestamp = timestamp

    elif 'wakes up' in event:
        if guardOnShift not in guardsAsleep:
            guardsAsleep[guardOnShift] = minutesAsleep(asleepTimestamp, timestamp)
        else:
            guardsAsleep[guardOnShift] += minutesAsleep(asleepTimestamp, timestamp)

        asleepTimestamp = ''

guardsAsleep = getGuardsAsleepMinutes(orderRecords(inputRecords))

print(getFrequentlyAsleepGuard(guardsAsleep))
