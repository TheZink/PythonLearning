number = int(input("Anna luku: "))

x = 1
while x+1 <= number:
    print(x)
    print(number)
    x +=1
    number -= 1

if x <= number:
    print(x)
