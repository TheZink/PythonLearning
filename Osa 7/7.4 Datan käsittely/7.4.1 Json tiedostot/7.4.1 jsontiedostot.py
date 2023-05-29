import json

def tulosta_henkilot(file_name: str):
    with open(file_name) as file:
        data = file.read()
    course = json.loads(data)

    for student in course:
        print(f"{student['nimi']} {student['ika']} vuotta ({', '.join(student['harrastukset'])})")


if __name__ == "__main__":
    tulosta_henkilot("tiedosto1.json")