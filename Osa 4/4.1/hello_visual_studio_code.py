while True:
    editor = input("Editori: ")
    if editor.lower() == "visual studio code":
        break
    if editor.lower() == "word" or editor.lower() == "notepad":
        print("surkea")
    else:
        print("ei ole hyvä")
print("loistava valinta!") 