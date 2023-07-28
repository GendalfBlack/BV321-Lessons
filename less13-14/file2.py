# словник (ключові слова)

client = {"lastname": "Прізвище", "name": "Ім'я", "phone": 992574613}

print(f"FIO: {client['lastname']} {client['name']}, {client['phone']}")

for key in client.keys():
    print(key, ":", client[key])

