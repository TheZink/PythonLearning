from math import sqrt

# Huomaa, että neliöjuuren voi laskea myös potenssin avulla:
# sqrt(9) on sama asia kuin 9 ** 0.5

anna1 = int(input("Anna a:"))
anna2 = int(input("Anna b:"))
anna3 = int(input("Anna c:"))

a,b,c = anna1, anna2, anna3

x = (-b + sqrt(b**2-4*a*c))/(2*a)
y = (-b - sqrt(b**2-4*a*c))/(2*a)

print(f"Juuret ovat {x} ja {y}")
