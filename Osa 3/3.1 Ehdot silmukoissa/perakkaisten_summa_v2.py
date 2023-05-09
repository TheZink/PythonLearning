#Tee perakkaisten_summa_v1 ohjelmasta hieman kehittyneempi versio, joka tulostaa 
#lopputuloksen lisäksi myös sen miten kyseinen summa lasketaan:
luku = int(input("Mihin asti: "))
num1 = 1
num2 = 1
num3 = ""
while num2 < luku:
    num1 += 1
    num2 += num1
    num3 += f" + {num1}"
print(f"Laskettiin 1{num3} = {num2}")

#Muuten sama kaavio, kuin mallivastauksessa (yllä), mutta rivin 10 sijaan
#käytin komentoa "num3 += " + " + str(num1)". Molemmat toimii samalla tavalla