#Tee ohjelma, joka lukee käyttäjältä kokonaisluvun ja kertoo sitten sen suuruusluokan

luku = int(input("Anna luku: "))

if luku < 1000:
    print("Luku on pienempi kuin 1000")

if luku < 100:
    print("Luku on pienempi kuin 100")

if luku < 10:
    print("Luku on pienempi kuin 10")

print("Kiitos!")