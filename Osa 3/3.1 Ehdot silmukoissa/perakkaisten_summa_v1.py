#Tee ohjelma, joka laskee peräkkäisten lukujen summaa 1 + 2 + 3 + ... 
#kunnes sen arvo on vähintään käyttäjän syöttämä luku.

luku = int(input("Mihin asti: "))
num1 = 1
num2 = 1
while num2 < luku:
    num1 += 1
    num2 += num1
print(num2)