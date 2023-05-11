from random import sample
from string import ascii_letters, digits
def luo_hyva_salasana(amount: int, digit, symbol):
    password = ""
    if digit is True:
        container = ascii_letters + digits
        number = numerial(amount, digit, symbol, container)
        return number
    elif symbol is True:
        container = ascii_letters
        punctuation = character(amount, digit, container)
        return punctuation
    else:
        alphabet = sample(ascii_letters, amount)
        for letter in alphabet:
            password += letter
        return password

def numerial(amount, digit, symbol, container): #Salasanaan lisätään numeroita
    if symbol is True:
        punctuation = character(amount,digit, container)
        return punctuation
    else:
        while True:
            a, b = False, False
            password = ""
            random_gen = sample(container, amount)
            for letter in random_gen:
                password += letter
            for check_number in password: #Tarkastetaan, onko salasanassa numeroita
                if check_number in digits: b = True 
            for check_letter in password: #Tarkastetaan, onko salasanassa kirjaimia
                if check_letter in ascii_letters: a = True
            if a is True and b is True:
                return password
            else:
                continue

def character(amount, digit, container): #Salasanaan lisätään erikoismerkkejä
    punctuation = "!?=+-()#"
    if digit is True: #Lisätään numeroita ja erikoismerkkejä
        while True:
            a, b, c = False, False, False
            password = ""
            container += punctuation
            random_gen = sample(container, amount)
            for letter in random_gen:
                password += letter
            for check_number in password: #Tarkastetaan, onko salasanassa numeroita
                if check_number in digits: b = True 
            for check_letter in password: #Tarkastetaan, onko salasanassa kirjaimia
                if check_letter in ascii_letters: a = True
            for check_sign in password: #Tarkastetaan, onko salasanassa erikoismerkkejä
                if check_sign in punctuation: c = True
            if a is True and b is True and c is True:
                return password
            else:
                continue
    else:
        while True: #Lisätään pelkästään erikoismerkkejä
            a, b= False, False
            password = ""
            container += punctuation
            random_gen = sample(container, amount)
            for letter in random_gen:
                password += letter
            for check_letter in password: #Tarkastetaan, onko salasanassa kirjaimia
                if check_letter in ascii_letters: a = True
            for check_sign in password: #Tarkastetaan, onko salasanassa erikoismerkkejä
                if check_sign in punctuation: b = True
            if a is True and b is True:
                return password
            else:
                continue

if __name__ == "__main__":
    for i in range(1):
        print(luo_hyva_salasana(20, True, True))


    
    
    

