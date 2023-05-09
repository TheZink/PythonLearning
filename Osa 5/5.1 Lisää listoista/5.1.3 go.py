def kumpi_voitti(game: list):
    player1 = 0
    player2 = 0
    tie = 0
    for element in game:
        for line in element:
            if line == 1:
                player1 += 1
            elif line == 2:
                player2 += 1
            elif line == 0:
                tie += 1
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0
if __name__ == "__main__":
    game = [[1,0,2],[1,1,2],[2,2,0],[1,1,1]]
    print(kumpi_voitti(game))
