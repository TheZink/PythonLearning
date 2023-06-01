from difflib import get_close_matches

def spellchecker():
    word_list = converter()
    
    text, text_wrong = "", []
    word_input = input("write text: ")
    word_input = word_input.split()

    for word in word_input:
        if word.lower() not in word_list:
            text += f"*{word}* "
            text_wrong.append(word.lower())
        else:
            text += f"{word} "
    
    if len(text_wrong) > 0: #Jos tekstissä on kirjoitusvirheitä, siirrytään "Find_matches"-funktioon
        check_list = find_matches(text_wrong, word_list)
        print(text)
        print("korjausehdotukset:")
        for word_key, word_value in check_list.items():
            text_suggestion = ""
            text_suggestion = ", ".join(word_value)
            text_suggestion = text_suggestion.replace('\n', '')
            print(f"{word_key}: {text_suggestion}")
    else: #Jos tekstissä ei ole kirjoitusvirheitä, niin tulostetaan teksti
        print(text)

def converter(): #Muuttaa txt-tiedoston listaksi
    wordlist = []
    with open("wordlist.txt") as file:
        for word in file:
            wordlist.append(word.strip())
    return wordlist

def find_matches(text_wrong, word_list): #Etsii listalta korjausehdotuksia
    suggestion = {}
    for word in text_wrong:
        check = get_close_matches(word, word_list)
        suggestion[word] = check
    return suggestion

spellchecker()

