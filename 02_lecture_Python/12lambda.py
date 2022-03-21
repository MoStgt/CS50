people = [
    {"name":"Harry", "house":"Gryffindor"},
    {"name": "Cho", "house": "Ravenclaw"},
    {"name": "Draco", "house": "Stytherin"}
]

def f(person):
    return person["house"]

people.sort(key=f)

print(people)