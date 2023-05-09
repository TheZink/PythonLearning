times1 = 0
times2 = 0
times3 = 1
shoes = []
index = int(input("Kuinka monta lukua: "))

while times1 < index:
    shoes.append(times1)
    times1 += 1

while times2 < index:
    size = int(input(f"Anna luku {times3}: "))
    shoes[times2] = size
    times2 += 1
    times3 += 1
print(shoes)


