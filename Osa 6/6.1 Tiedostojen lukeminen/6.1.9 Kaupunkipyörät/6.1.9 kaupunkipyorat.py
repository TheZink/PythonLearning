import math
def hae_asematiedot(locations: str): #funktio purkaa csv-tiedoston, poimii pyörä-aseman nimen sekä koordinaatit(tuple) sekä tallentaa ne dict-listaan
    stations = {}
    with open(locations) as file:
        for bike_stations in file:
            row = bike_stations.split(";")
            if row[0] == "Longitude":
                continue
            stations[row[3]] = (float(row[0]), float(row[1]))
        return stations

def etaisyys(position: dict, stations1: str, stations2: str): #funktio laskee pyörä-asemien kordinaatit ja laskee asemien etäisyydet
    long1, long2 = 0, 0 
    lat1, lat2 = 0, 0
    if stations1 in position:
        long1 = position[stations1][0]
        lat1 = position[stations1][1]
    if stations2 in position:
        long2 = position[stations2][0]
        lat2 = position[stations2][1]
    longitude = (long1 - long2) * 55.26
    latitude = (lat1 - lat2) * 111.2
    result = math.sqrt(longitude**2 + latitude**2)
    return result

def suurin_etaisyys(position: dict):
    stations1, stations2, distance = "", "", 0
    for row_a, pos_a in position.items():
        long_a, lat_a = pos_a[0], pos_a[1]
        for row_b, pos_b in position.items():
            if row_b == row_a:
                continue
            long_b, lat_b = pos_b[0], pos_b[1]
            longitude = (long_a - long_b) * 55.26
            latitude = (lat_a - lat_b) * 111.2
            result = math.sqrt(longitude**2 + latitude**2)
            if result > distance:
                stations1 = row_a
                stations2 = row_b
                distance = result
    return(stations1, stations2, distance)


if __name__  == "__main__":
    stations = hae_asematiedot("stations1.csv")
    print(stations)
    distance = etaisyys(stations, "Viiskulma", "Kaivopuisto")
    print(distance)
    range = suurin_etaisyys(stations)
    print(range)