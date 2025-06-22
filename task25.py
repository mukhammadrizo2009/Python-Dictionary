def group_by_age(people: list[dict[str, int | str]]) -> dict[int, list[str]]:
    result = {}

    for person in people:
        age = person["age"]
        name = person["name"]

        if age not in result:
            result[age] = []

        result[age].append(name)
    return result
    
people = [
    {"name": "Ali", "age": 12},
    {"name": "Vali", "age": 15},
    {"name": "Hasan", "age": 12},
    {"name": "Husan", "age": 15},
    {"name": "Karim", "age": 17}
]

result = (group_by_age(people))
print(result)
