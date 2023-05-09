#Saat seuraavan koodinpätkän työnhakijoille suunnatun sovelluksen parissa työskentelevältä tuttavaltasi.
#Koodi toimii melkein oikein, mutta ei kuitenkaan ihan. Tässä tehtävässä on todella tarkat testit, jotka vaativat, että tulostus on välilyönnilleen oikein.

#Korjaa siis koodi siten, että tulostus näyttää oikealta. Huomaa, että erityisesti print-komennon muoto
#jossa tulostettavat osat eritellään pilkulla, voi tuottaa yllätyksiä, sillä se lisää osien väliin välilyönnin.

#Helpoiten saat muutettua koodin toimivaksi käyttämällä tulostukseen f-merkkijonoja.
#Vihje: saat tulostettua tyhjän rivin komennolla print tai lisäämällä tulostettavaan merkkijonoon merkinnän \n.

nimi = "Teppo Testaaja"
ika = 20
taito1 = "python"
taso1 = "aloittelija"
taito2 = "java"
taso2 = "veteraani"
taito3 = "ohjelmointi"
taso3 = "puoliammattilainen"
ala = 2000
yla = 3000

print(f"nimeni on {nimi}, olen {ika}-vuotias\n")
print("taitoihini kuuluvat")
print(f" - {taito1} ({taso1})")
print(f" - {taito2} ({taso2})")
print(f" - {taito3} ({taso3})\n")
print(f"haen työtä, josta maksetaan palkkaa {ala}-{yla} euroa kuussa")
