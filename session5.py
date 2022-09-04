import csv

with open('coaches.csv', 'r') as coaches_file:
    reader = csv.DictReader(coaches_file)
    lazy_coaches = [
        coach for coach in reader if int(coach['sessions_delivered']) < 14
    ]

with open('lazy_coaches.csv', 'w') as lazy_file:
    writer = csv.DictWriter(lazy_file, ['course', 'name', 'sessions_delivered'])
    writer.writeheader()
    writer.writerows(lazy_coaches)

name,course,sessions_delivered
Peter,Software CFGDegree,12
Anca,Software CFDegree,10
Alex,Software CFDegree,14
