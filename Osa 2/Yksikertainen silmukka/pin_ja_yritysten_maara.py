time = 0

while True:
    pin = int(input("PIN-koodi: "))
    time += 1

    if pin == 4321 and time == 1:
        print("Oikein, tarvitsit vain yhden yrityksen!")
        break
    
    if pin == 4321:
        print(f"Oikein, tarvitsit {time} yritystä")
        break
    else:
        print("Väärin")

