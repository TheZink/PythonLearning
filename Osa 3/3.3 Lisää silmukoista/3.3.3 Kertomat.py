while True:
    number = int(input("Anna luku: "))
    index = 1
    x = 1
    y = 2
    if number <= 0:
        print("Kiitos ja moi!")
        break
    while index < number:
        x = x * y
        y += 1
        index += 1
    print(f"Luvun {number} kertoma on {x}")
