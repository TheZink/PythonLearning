from random import choice
def heita(dice: str):
    dice_a, dice_b, dice_c = [3,3,3,3,3,6], [2,2,2,5,5,5], [1,4,4,4,4,4]
    if dice == "A": return choice(dice_a)
    if dice == "B": return choice(dice_b)
    if dice == "C": return choice(dice_c)

def pelaa(dice1: str, dice2: str, times: int):
    dice1_win, dice2_win, tie = 0, 0, 0
    while True:
        for round in range(times):
            if heita(dice1) > heita(dice2): dice1_win += 1
            if heita(dice2) > heita(dice1): dice2_win += 1
            if heita(dice1) == heita(dice2): tie += 1
        if dice1_win + dice2_win == times or dice1_win + dice2_win + tie == times:
            return (dice1_win, dice2_win, tie)
        else:
            dice1_win, dice2_win, tie, round = 0, 0, 0, 0

if __name__ == "__main__":
    tulos = pelaa("A", "B", 100)
    print(tulos)