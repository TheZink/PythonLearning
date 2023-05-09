def converter():
    with open("wordlist.txt") as file:
        for word in file:
            checklist.append(word.strip())
    return checklist

def spellchecker():
    check = ""
    word = input("Write text: ")
    a = word.split()
    for b in a:
        if b.lower() in checklist:
            check += f"{b} "
        else:
            check += f"*{b}* "
    print(check)
            
checklist = []
converter()
spellchecker()