users = [{
    "name": "ali",
    "age" : 16
    },
    {
    "name": "vali",
    "age" : 15
    },
    {
    "name": "sami",
    "age" : 17
    },
    {
    "name": "joni",
    "age" : 18
    },
]

oldest_user = users[0]
for user in users:
    if user['age'] > oldest_user['age']:
        oldest_user = user

print(f"ism {oldest_user['name']}, yoshi {oldest_user['age']}")