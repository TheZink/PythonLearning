from string import ascii_letters, punctuation
def jaa_merkkeihin(string: str):
    letters = ""
    special_characters = ""
    other = ""
    for character in string:
        if character in ascii_letters:
            letters += character
        elif character in punctuation:
            special_characters += character
        else:
            other += character
    return letters, special_characters, other

    
if __name__ == "__main__":
    part = jaa_merkkeihin("Tämä on testi!!! Toimiiko, mitä?")
    print(part[0])
    print(part[1])
    print(part[2])
