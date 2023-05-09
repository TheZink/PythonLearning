x = int(input("Kerro ikäsi?: "))

if x >= 5 and x <= 99:
    print(f"Ok, olet siis {x}-vuotias")

elif x >= 0 and x <= 5:
    print("En usko, että osaat kirjoittaa...")

elif x <= 0:
    print("Taitaa olla virhe")

