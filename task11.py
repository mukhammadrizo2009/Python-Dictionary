config = {}

for i in range(3):
    name = input(f"{i+1} - Setting nomini kirting!: ")
    value = input(f"{i+1} - Qiymatni kiriting!: ")
    config[name] = value

print("Natija: ",config)