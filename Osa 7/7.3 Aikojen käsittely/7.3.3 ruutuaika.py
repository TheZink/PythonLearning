from datetime import datetime, timedelta

file_name = input("Tiedosto: ")
date_number = input("aloituspäivä: ")
lenght_days = int(input("Montako päivää: "))
print("Anna ruutuajat kunakin päivänä minuutteina (TV tietokone mobiililaite):")

time_total, times = 0, 0
data = []

while times != lenght_days: #Funktio tallentaa käyttäjän syötteet listaan sekä lasketaan ruutuaika
    date_time= datetime.strptime(date_number, "%d.%m.%Y")
    end_time = date_time + timedelta(days=times)
    screen_input = input(f"Ruutuaika {end_time.strftime('%d.%m.%Y')}: ").split(" ")
    for a in screen_input:
        time_total += int(a)
    times += 1
    data.append(f"{end_time.strftime('%d.%m.%Y')}: {screen_input[0]}/{screen_input[1]}/{screen_input[2]}")

with open(file_name, "w") as file: #Tiedot puretaan ja tallennetaan tiedostoon
    file.write(f"Ajanjakso: {date_time.strftime('%d.%m.%Y')}-{end_time.strftime('%d.%m.%Y')}\n")
    file.write(f"Yht. minuutteja: {time_total}\n")
    file.write(f"Keskim. minuutteja: {time_total/lenght_days}\n")
    for row in data:
        file.write(f"{row}\n")
    print(f"Tiedosto tallennettu tiedostoon {file_name}")

