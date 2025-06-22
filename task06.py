person = {
    "first_name": "G'ani",
    "last_name": "Abdug'aniyev",
    "age": "23",
    "country": "the USA",
    "phone": "+1 23 412 2341",
    "email": "gani41@gmail.com"
}

keys = input("Kalit nomini kiriting!: ")


if keys in person:
    print("Natija:",person[keys])

else:
    print("Kalit topilmadi!")