# https://www.algoexpert.io/questions/tournament-winner
def tournament_winner(competitions, results):
    victories = {}
    for i in range(0, len(competitions)):
        winner = competitions[i][abs(results[i] - 1)]
        victories[winner] = victories.get(winner, 0) + 1
    print(max(victories.keys(), key=lambda k: victories[k]))


