def muotoile(lista=list):
    palautus = []
    varasto = ""
    for i in lista:
        varasto += str(f"{i:.2f}")
        palautus.append(varasto)
        varasto = ""
    
    return (palautus)

if __name__ == "__main__":
    lista = [1.234, 0.3333, 0.11111, 3.446]
    lista2 = muotoile(lista)
    print(lista2)

#def muotoile(lista: list):
    #tulos = []
 
    #for luku in lista:
        #tulos.append(f"{luku:.2f}")
 
    #return tulos