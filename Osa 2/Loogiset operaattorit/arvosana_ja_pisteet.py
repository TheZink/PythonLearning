x = int(input("Anna pisteet [0-100]: "))

if x == 0 or x >= 0 and x <= 49:
    print("Arvosana: hylätty")

elif x == 50 or x >= 50 and x <= 59:
    print("Arvosana: 1")

elif x == 60 or x >= 60 and x <= 69:
    print("Arvosana: 2")

elif x == 70 or x >= 70 and x <= 79:
    print("Arvosana: 3")

elif x == 80 or x >= 80 and x <=89:
    print("Arvosana: 4")

elif x == 90 or x >= 90 and x < 100 or x == 100:
    print("Arvosana: 5")

else:
    print("Arvosana: mahdotonta!")