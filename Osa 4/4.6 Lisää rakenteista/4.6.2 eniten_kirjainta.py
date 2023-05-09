def eniten_kirjainta(mjono):
    a = ""
    time = 0
    monta = 0
    for i in mjono:
        monta = mjono.count(i)
        if mjono.count(i) > time:
            a = i
            time = monta
    return a

if __name__ == "__main__":
    mjono = "esimerkkimerkkijonokki"
    print(eniten_kirjainta(mjono))

#def eniten_kirjainta(mjono: str):
    #yleisin = mjono[0]
    #for kirjain in mjono:
        #if mjono.count(kirjain) > mjono.count(yleisin):
           # yleisin = kirjain
 
    #return yleisin