number = int(input("Anna luku: "))

x = 1
while x+1 <= number:
    print(x + 1)
    print(x)
    x += 2

if x <= number:
    print(x)