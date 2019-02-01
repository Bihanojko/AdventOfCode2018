# 404 players; last marble is worth 71852 points

PLAYER_COUNT = 404
LAST_MARBLE_WORTH = 71852 * 100

playerScores = [0 for _ in range(PLAYER_COUNT)]
placedMarbles = [0]
currentMarble = 0

for marbleID in range(1, LAST_MARBLE_WORTH + 1):
    if marbleID % 100000 == 0:
        print(marbleID)

    prevLength = len(placedMarbles)

    if marbleID % 23 == 0:
        playerScores[marbleID % PLAYER_COUNT - 1] += marbleID + placedMarbles[(currentMarble - 7) % prevLength]
        del placedMarbles[(currentMarble - 7) % prevLength]
        currentMarble = (currentMarble - 7) % prevLength

    else:
        placedMarbles = placedMarbles[: (currentMarble + 1) % prevLength + 1] + [marbleID] + placedMarbles[(currentMarble + 1) % prevLength + 1 :]
        currentMarble = (currentMarble + 1) % prevLength + 1

print('')
print(max(playerScores))
