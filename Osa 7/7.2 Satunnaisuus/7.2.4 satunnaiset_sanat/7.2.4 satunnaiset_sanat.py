from random import sample
def sanat(amount: int, search: str):
    word_list = []
    with open("sanat.txt") as file:
        for row in file:
            if row.startswith(search):
                if row not in word_list:
                    row = row.strip()
                    word_list.append(row)
        word_pick = sample(word_list, amount)
        return word_pick

if __name__ == "__main__":
    test = sanat(3, "ca")
    print(test)