dictionary = {}
while True:
    commands = int(input("komento (1 hae, 2 lisää, 3 lopeta): "))
    if commands == 1:
        a = input("nimi: ")
        if a in dictionary:
            print(dictionary[a])
        else:
            print("ei numeroa")
    if commands == 2:
        b = input("nimi: ")
        c =(input("numero: "))
        if b in dictionary:
            dictionary[b] += f"\n{c}"
        else:
            dictionary[b] = f"{c}"
        print("ok!")
    if commands == 3:
        print("lopetetaan...")
        break
# def hae(henkilot):
#     nimi = input("nimi: ")
#     if nimi in henkilot:
#         for numero in henkilot[nimi]:
#             print(numero)
#     else:
#         print("ei numeroa")
 
# def lisaa(henkilot):
#     nimi = input("nimi: ")
#     numero = input("numero: ")
#     if nimi not in henkilot:
#         henkilot[nimi] = []
#     henkilot[nimi].append(numero)
#     print("ok!")
 
# def main():
#     henkilot = {}
#     while True:
#         komento = input("komento (1 hae, 2 lisää, 3 lopeta): ")
#         if komento == "1":
#             hae(henkilot)
#         if komento == "2":
#             lisaa(henkilot)
#         if komento == "3":
#             break
#     print("lopetetaan...")
 
# main()