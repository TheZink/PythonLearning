list = []
time = 0

while True:
    a = input("sana: ")
    if a in list:
        print(f"Annoit {time} eri sanaa")
        break
    list.append(a)
    time += 1