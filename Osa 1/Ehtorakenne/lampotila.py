#Tee ohjelma, joka kysyy käyttäjältä lämpötilan fahrenheit-asteina, ja tulostaa sitten lämpötilan celsius-asteina.
#Jos lämpötila celsius-asteina on pienempi kuin 0, ohjelma tulostaa lisäksi viestin "Paleltaa!".
#Kaavan fahrenheit-asteiden muuntamiseksi celsius-asteiksi voit etsiä esimerkiksi googlaamalla.

temp = float(input("Anna lämpötila (F): "))

if temp > 32:
    print(f"{temp} fahrenheit-astetta on {(temp-32)/1.8} celsius-astetta")

elif temp < 32:
    print(f"{temp} fahrenheit-astetta on {(temp-32)/1.8} celsius-astetta")
    print("Paleltaa!")

else:
    print(f"{temp} fahrenheit-astetta on {(temp-32)/1.8} celsius-astetta")

#if temp == 32:
    #print(f"{temp} fahrenheit-astetta on {(temp-32)/1.8} celsius-astetta")