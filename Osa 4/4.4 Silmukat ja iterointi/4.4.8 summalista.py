def summa(a = list, b = list):
    time = 0
    lista = []
    for i in a:
        lista.append(i + b[time])
        time += 1
    return lista
if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    vastaus = summa(a,b)
    print(vastaus) # [8, 10, 12]

#def summa(lista1: list, lista2: list):
    #tulos = []
    #for i in range(len(lista1)):
        #tulos.append(lista1[i] + lista2[i])
 
    #return tulos
# Toinen ratkaisu olisi hyödyntää zip-funktiota,
# joka luo uuden listan yhdistämällä kahden tai useamman listan alkiot:
# for alkio1, alkio2 in zip(lista1, lista2):
#   tuloslista.append(alkio1 + alkio2)
# tee ratkaisu tänne
