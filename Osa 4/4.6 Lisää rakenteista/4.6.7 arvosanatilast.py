arvosana = [0, 0, 0, 0, 0, 0]
tulos = []
def koe_harjoitus_luvut(): #funktio laskee käyttäjän syöttämät luvut (koepisteet ja suoritetut harjoitustehtävät), jonka jälkeen vie luvut "tulos"-listaan
    while True:
        kpl = input("Koepisteet ja harjoitusten määrä: ")
        if kpl == "": return tulos
        a = kpl.split() 
        b = int(a[1])//10; a[1] = b #muuttaa indeksin[1] ja palauttaa sen muutettuna
        x = 0
        for i in a: #Laskee alkiot yhteen, jonka jälkeen palaa takaisin alkuun
            x += float(i)
        if x >= 0 and x <= 14 or int(a[0]) < 10: arvosana[0] += 1 # Asteikko 0 (hylätty)
        elif x >= 15.0 and x <= 17.9: arvosana[1] += 1 # Asteikko 1
        elif x >= 18.0 and x <= 20.9: arvosana[2] += 1 # Asteikko 2
        elif x >= 21.0 and x <= 23.9: arvosana[3] += 1 # Asteikko 3
        elif x >= 24.0 and x <= 27.9: arvosana[4] += 1 # Asteikko 4
        elif x >= 28.0 and x <= 30.0: arvosana[5] += 1 # Asteikko 5
        tulos.append(x)
 
def tuloksen_laskenta(tulos):
    hyvaksytty = sum(arvosana) - arvosana[0]
    tahti = "*"
    print(f"Tilasto:\nPisteiden keskiarvo: {sum(tulos)/len(tulos):.1f}\nHyväksymisprosentti: {hyvaksytty/len(tulos)*100:.1f}\nArvosanajakauma:")
    print(f" 5: {arvosana[5]*tahti} \n 4: {arvosana[4]*tahti} \n 3: {arvosana[3]*tahti} \n 2: {arvosana[2]*tahti} \n 1: {arvosana[1]*tahti} \n 0: {arvosana[0]*tahti}" )
        
tulos = koe_harjoitus_luvut()
raportti = tuloksen_laskenta(tulos)