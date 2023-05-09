def nelio(x,y):
    time = y
    word = (x * y)*y
    while time > 0:
        print(word[0:y])
        word = word[y:]
        time -= 1