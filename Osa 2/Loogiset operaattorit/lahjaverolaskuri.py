x = float(input("Lahjan suuruus? "))

if x < 5000:
    print("Ei veroa!")
elif x == 5000 or x >=5000 and x <= 25000:
    print("Vero:",(100+(x-5000)*0.08))
elif x == 25000 or x >= 25000 and x <= 55000:
    print("Vero:",(1700+(x-25000)*0.10))
elif x == 55000 or x >= 55000 and x <= 200000:
    print("Vero:",(4700+(x-55000)*0.12))
elif x == 200000 or x >= 200000 and x <= 1000000:
    print("Vero:",(22100+(x-200000)*0.15))
elif x == 1000000 or x >= 1000000:
    print("Vero:",(142100+(x-1000000)*0.17))