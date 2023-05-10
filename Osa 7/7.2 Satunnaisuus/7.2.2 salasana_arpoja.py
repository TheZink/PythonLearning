from random import sample
from string import ascii_lowercase
def luo_salasana(amount: int):
    password = ""
    character = sample(ascii_lowercase, amount)
    for letter in character:
        password += letter
    return password

if __name__ == "__main__":
    for i in range(10):
        print(luo_salasana(8))
