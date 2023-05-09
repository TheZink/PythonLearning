luku = int(input("Anna luku: "))
x = 1
while x <= luku:
    y = 1
    while y <= luku:
        print(f"{x} x {y} = {x*y}")
        y += 1
    x += 1