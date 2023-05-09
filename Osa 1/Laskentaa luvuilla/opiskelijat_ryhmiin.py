#Tee ohjelma, joka kysyy kurssin opiskelijoiden määrän ja ryhmän koon ja ilmoittaa,
#montako ryhmää opiskelijoista muodostuu. Jos jako ei mene tasan, yhdessä ryhmässä
#voi olla vähemmän opiskelijoita, mutta kaikissa muissa on oltava haluttu määrä.

#Vihje: tehtävän tekeminen onnistuu kokonaislukujakolaskuoperaattorilla //

student = float(input("Montako opiskelijaa? "))
group = float(input("Mikä on ryhmän koko? "))

if student > 100:
    a = student // group
    b = int('%.0f' % a)
    print("Ryhmien määrä: ", int(b + 1))

if student < 100:
    x = student / group
    y = '%.0f' % x
    print(f"Ryhmien määrä: {y}")