import urllib.request, json, math

def hae_kaikki():
    request_site = urllib.request.urlopen("https://studies.cs.helsinki.fi/stats-mock/api/courses")
    data = request_site.read()
    course = json.loads(data)
    ongoing = []
    for a in course:
        scores = 0
        if a['enabled'] is True:
            for number in a['exercises']:
                scores += int(number)
            ongoing.append((a['fullName'], a['name'], a['year'], scores))
    return ongoing


def hae_kurssi(course: str):
    request_site = urllib.request.urlopen(f"https://studies.cs.helsinki.fi/stats-mock/api/courses/{course}/stats")
    data = request_site.read()
    course = json.loads(data)
    week, students, hours, hours_avg, exer, exer_avg = len(course), 0, 0, 0, 0, 0
    for courses in course:
        if int(course[courses]['students']) > students:
            students += int(course[courses]['students'])
        exer += int(course[courses]['exercise_total'])
        hours += int(course[courses]['hour_total'])
    hours_avg = hours / students
    exer_avg = exer / students

    return {'viikkoja': week,
            'opiskelijoita': students,
            'tunteja': hours,
            'tunteja_keskimaarin': math.floor(hours_avg),
            'tehtavia': exer,
            'tehtavia_keskimaarin': math.floor(exer_avg)
    }

if __name__ == "__main__":
    hae_kaikki()
    hae_kurssi("docker2019")