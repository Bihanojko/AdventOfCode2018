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
        asleep.append(minuteAsleep)
        minuteAsleep += datetime.timedelta(minutes = +1)

    return asleep


def getGuardsAsleepTimestamps(orderedRecords):
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


def getMostAsleepGuardID(guardsAsleep):
    guardMostAsleepID = -1
    guardMostAsleepMinutes = -1

    for guardID in guardsAsleep:
        if guardMostAsleepMinutes < len(guardsAsleep[guardID]):
            guardMostAsleepMinutes = len(guardsAsleep[guardID])
            guardMostAsleepID = guardID

    return guardMostAsleepID


def getMostAsleepMinute(guardAsleep):
    minutesAsleep = {}

    for minuteAsleep in guardAsleep:
        if minuteAsleep.minute in minutesAsleep:
            minutesAsleep[minuteAsleep.minute] += 1
        else:
            minutesAsleep[minuteAsleep.minute] = 1

    return max(minutesAsleep.items(), key=operator.itemgetter(1))[0]


inputFile = open('input', 'r')
inputRecords = inputFile.readlines()
inputFile.close()


guardsAsleep = getGuardsAsleepTimestamps(orderRecords(inputRecords))

guardMostAsleepID = getMostAsleepGuardID(guardsAsleep)
mostAsleepMinute = getMostAsleepMinute(guardsAsleep[guardMostAsleepID])

print(int(guardMostAsleepID) * mostAsleepMinute)
