def lue(a, b, c):
    while True:
        try:
            number = int(input(a))
            if number > b and number < c:
                return number
        except:
            pass
        print(f"Syötteen on oltava kokonaisluku väliltä {b}...{c}")

if __name__ == "__main__":
    number = lue("anna luku: ",5, 10)
    print("syötit luvun: ", number)