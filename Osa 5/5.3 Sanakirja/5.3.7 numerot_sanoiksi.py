def lukukirja():
    numbers = {0: "nolla", 1: "yksi", 2:"kaksi", 3:"kolme", 4:"neljä", 5:"viisi", 6:"kuusi", 7:"seitsemän", 8:"kahdeksan", 9:"yhdeksän", 10:"kymmenen"}
    new_numb = {}
    key, num1,  num2 = 11,1,1
    for a, b in numbers.items():
        new_numb[a] = b
    while key <= 99:
        while key <= 19:
            new_numb[key] = f"{numbers[num2]}toista"
            key += 1
            num2 += 1
        num2 = 1
        num1 += 1
        if key >= 20:
            new_numb[key] = f"{numbers[num1]}kymmentä"
            key += 1
        while key > 20 and key <= 29:
            new_numb[key] = f"{numbers[num1]}kymmentä{numbers[num2]}"
            key += 1
            num2 += 1
        while key > 30 and key <= 39:
            new_numb[key] = f"{numbers[num1]}kymmentä{numbers[num2]}"
            key += 1
            num2 += 1
        while key > 40 and key <= 49:
            new_numb[key] = f"{numbers[num1]}kymmentä{numbers[num2]}"
            key += 1
            num2 += 1
        while key > 50 and key <= 59:
            new_numb[key] = f"{numbers[num1]}kymmentä{numbers[num2]}"
            key += 1
            num2 += 1
        while key > 60 and key <= 69:
            new_numb[key] = f"{numbers[num1]}kymmentä{numbers[num2]}"
            key += 1
            num2 += 1
        while key > 70 and key <= 79:
            new_numb[key] = f"{numbers[num1]}kymmentä{numbers[num2]}"
            key += 1
            num2 += 1
        while key > 80 and key <= 89:
            new_numb[key] = f"{numbers[num1]}kymmentä{numbers[num2]}"
            key += 1
            num2 += 1
        while key > 90 and key <= 99:
            new_numb[key] = f"{numbers[num1]}kymmentä{numbers[num2]}"
            key += 1
            num2 += 1
       
     
    return new_numb

if __name__ == "__main__":
    luvut = lukukirja()
    print(luvut[2])
    print(luvut[11])
    print(luvut[45])
    print(luvut[99])
    print(luvut[0])