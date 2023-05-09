def eka_sana(lause):
    sana = ""
    while lause != " ":
        a = lause.find(" ")
        sana = lause[0:a]
        return sana
    

def toka_sana(lause):
    sana = ""
    a = lause.find(" ")
    sana += lause[a+1:]
    b = sana.find(" ")
    while True:
        if b > 0:
            c = sana.find(" ")
            sana = sana[0:c]
        else:
            sana = sana[0:]
        return sana

def vika_sana(lause):
    while lause.find(" ") > 0:
        a = lause.find(" ")
        lause = lause[a+1:]
    return lause



if __name__ == "__main__":
    lause = "olipa kerran kauan sitten ohjelmoija"
    print(eka_sana(lause))
    print(toka_sana(lause))
    print(vika_sana(lause))