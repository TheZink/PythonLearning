from datetime import datetime
def millenium():
    day, month, year = int(input("Päivä: ")), int(input("Kuukausi: ")), int(input("Vuosi: "))
    millenium_date = datetime(1999, 12, 31) - datetime(year, month, day)
    return millenium_date.days


age = millenium()
if age > 0:
    print(f"Olit {age} päivää vanha, kun vuosituhat vaihtui.") 
else:
    print("Et ollut syntynyt, kun vuosituhat vaihtui.")