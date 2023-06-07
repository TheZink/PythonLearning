from string import ascii_letters, digits
def vaihda_koko(Sentence: str):
    word = ""
    for letter in Sentence:
        if letter.isupper() is True:
            word += letter.lower()
        else:
            word += letter.upper()
    return word

def puolita(Sentence: str):
    one, two = "", ""
    summary = len(Sentence) // 2 - 1
    for number in range(len(Sentence)):
        if number <= summary:
            one += Sentence[number]
        else:
            two += Sentence[number]
    return one, two

def poista_erikoismerkit(Sentence: str):
    word = ""
    ascii_fin = "ABCDEFGHIJKLMNOPQRSŠTUVWXYZŽÅÄÖabcdefghijklmnopqrstuvwyzåäö0123456789 "
    for letter in Sentence:
        if letter in ascii_fin:
            word += letter
        else:
            continue
    return word

if __name__ == "__main__":
    test = poista_erikoismerkit("Tämäkö on testi")
    print(test)
