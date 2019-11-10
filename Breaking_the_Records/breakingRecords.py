def breakingRecords(scores):
    highestscore = [scores[0]]
    lowestscore = [scores[0]]

    for n in range(1, len(scores)):
        if scores[n] > highestscore[len(highestscore)-1]:
            highestscore.append(scores[n])

    for n in range(1, len(scores)):
        if scores[n] < lowestscore[len(lowestscore)-1]:
            lowestscore.append(scores[n])

    return len(highestscore)-1, len(lowestscore)-1


scoresArray = [10, 5, 20, 20, 4, 5, 2, 25, 1]
# scoresArray = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
print(breakingRecords(scoresArray))
