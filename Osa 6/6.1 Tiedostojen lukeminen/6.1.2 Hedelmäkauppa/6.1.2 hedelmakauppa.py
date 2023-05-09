def lue_hedelmat():
    with open("hedelmat.csv") as file:
        product = {}
        for fruits in file:
            fruits = fruits.replace("\n", "")
            column = fruits.split(";")
            product[column[0]] = float(column[1])
    print(product)
    return product
if __name__ == "__main__":
    lue_hedelmat()