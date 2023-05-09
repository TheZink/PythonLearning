def pelaa_siirto(lauta: list, a: int, b: int, place: str):
    if a < 0 or a > 2 or b < 0 or b > 2:
       return False
    if lauta[b][a] == '':
        lauta[b][a] = place
        return True
    else:
        return False
     

if __name__ == "__main__":
    lauta = [['', '', 'X'], ['', '', ''], ['', '', '']]
    print(pelaa_siirto(lauta, 0, 3, "X"))
    print(lauta)