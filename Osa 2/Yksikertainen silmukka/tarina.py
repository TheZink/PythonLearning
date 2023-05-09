sanat = ""
while True:
    sana = input("Anna sana: ")
    if sana == "loppu":
        break
    if len(sanat) and sanat.split()[-1] == sana:
        break
    sanat += sana + " "
sanat = sanat.replace("loppu", "")
print(sanat)

#sanat = ""
#same = ""
#while True:
    #sana = input("Anna sana: ")
    #if sana == "loppu" or sana == same:
        #break
    #sanat += sana + " "
    #same = sana

#print(sanat)