list = []
x = 1
while True:
    print(f"Lista on nyt {list}")
    a = input("(l)isää, (p)oista vai e(x)it: ")
    if a == "l":
        list.append(x)
        x += 1
    if a == "p":
        x -= 1
        list.remove(x)
    if a == "x":
        print("Moi!")
        break