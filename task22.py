def group_students(students: list[dict[str, str]]) -> dict[str, list[str]]:
    groups = {}
    for student in students:
        groups.setdefault(student['group'], []).append(student['name'])
    return  groups


students = [
    {
        "name": "Ali",
        "group": "A"
    },
        {
        "name": "Vali",
        "group": "B"
    },    {
        "name": "Bob",
        "group": "C"
    },    {
        "name": "Jon",
        "group": "A"
    },
]

result = group_students(students)
print(result)