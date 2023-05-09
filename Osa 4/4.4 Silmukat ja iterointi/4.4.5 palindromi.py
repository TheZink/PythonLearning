def palindromi(sana):
    reverse = sana[-1::-1]
    if reverse == sana:
        return True
    else:
        return False

while True:
    sana = input("Anna sana: ")
    b = ""
    palindromi(sana)
    for i in sana:
        b = i + b
    if sana == b:
        print(f"{sana} on palindromi!")
        break
    else:
        print("ei ollut palindromi")
