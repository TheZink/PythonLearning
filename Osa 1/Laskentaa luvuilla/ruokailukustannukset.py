#Tee ohjelma, joka arvioi käyttäjän keskimääräisiä ruokailukustannuksia.
#Ohjelma kysyy, kuinka monta kertaa viikossa käyttäjä käy Unicafessa ja Unicafe-lounaan hinnan sekä viikon muiden ruokaostosten hinnan.
#Näiden tietojen perusteella ohjelma laskee käyttäjän keskimääräiset ruokamenot sekä viikossa että yhtenä päivänä.

uni = int(input("Montako kertaa viikossa syöt Unicafessa?"))
hinta = float(input("Unicafe-lounaan hinta?"))
ruoka = float(input("Paljonko käytät viikossa ruokaostoksiin?"))

cafe = uni * hinta
summa = ruoka + cafe
paiva = summa / 7

print("")
print("Kustannukset keskimäärin:")
print(f"Päivässä {paiva} euroa")
print(f"Viikossa {summa} euroa")