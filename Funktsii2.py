import collections 

pets = {
    0: {
        "Текст": {
            "Вид питомца": "Тестовый",
            "Возраст питомца": 1,
            "Имя владельца": "Админ"
        }
    }
}

def get_suffix(age):
    last_digit = age % 10
    last_two_digits = age % 100

    if 11 <= last_two_digits <= 14:
        return "лет"
    elif last_digit == 1:
        return "год"
    elif 2 <= last_digit <= 4:
        return "года"
    else:
        return "лет"

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False

def pets_list():
    print("\n--- Список всех питомцев ---")
    for ID in pets:
        if ID == 0:
            continue

        for name in pets[ID]:
            info = pets[ID][name]
            suffix = get_suffix(info["Возраст питомца"])
            print(f'ID {ID}: Это {info["Вид питомца"]} по кличке "{name}". '
                  f'Возраст питомца: {info["Возраст питомца"]} {suffix}. '
                  f'Имя владельца: {info["Имя владельца"]}')
    print("----------------------------\n")

def create():
    last = collections.deque(pets, maxlen=1)[0]
    new_id = last + 1 

    print("\n[Добавление нового питомца]")
    name = input("Введите имя питомца: ")
    kind = input("Введите вид питомца: ")
    age = int(input("Введите возраст питомца: "))
    owner = input("Введите  имя владельца: ")

    pets[new_id] = {
        name: {
            "Вид питомца": kind,
            "Возраст питомца": age,
            "Имя владельца": owner
        }
    }
    print(f"Успешно добавлено! Питомцу присвоен ID: {new_id}\n")

def read():
    print("\n[Просмотр информации]")
    ID = int(input("Введите ID питомца: "))
    pet_data = get_pet(ID)

    if pet_data == False or ID == 0:
        print("Ошибка: Питомца с таким ID не существует!\n")
    else:
        for name in pet_data:
            info = pet_data[name]
            suffix = get_suffix(info["Возраст питомца"])
            print(f'Это {info["Вид питомца"]} по кличке "{name}. '
                  f'Возраст питомца: {info["Возраст питомца"]} {suffix}. '
                  f'Имя владельца: {info["Имя владельца"]}\n')

def update():
    print("\n[Редактирование записи]")
    ID = int(input("введите ID питомца для изменения: "))
    pet_data = get_pet(ID)

    if pet_data == False or ID == 0:
        print("Ошибка: Питомца с таким ID не существует!\n")
    else:
        old_name = list(pet_data.keys())[0]

        print("Введите новые данные (или старые, если менять не нужно):")
        new_name = input(f"Имя питомца (сейчас {old_name}): ")
        new_kind = input(f"Вид питомца (сейчас {pet_data[old_name]['Вид питомца']}): ")
        new_age = int(input(f"Возраст питомца (сейчас {pet_data[old_name]['Возраст питомца']}): "))
        new_owner = input(f"Имя владельца (сейчас {pet_data[old_name]['Имя владельца']}): ")

        del pets[ID][old_name]
        pets[ID][new_name] = {
            "Вид питомца": new_kind,
            "Возраст питомца": new_age,
            "Имя владельца": new_owner
        }
        print("Данные успешно обновлены!\n")

def delete():
    print("\n[Удаление записи]")
    ID = int(input("Введите ID питомца для удаления: "))
    pet_data = get_pet(ID)

    if pet_data == False or ID == 0:
        print("Ошибка: Питомца с таким ID не существует!\n")
    else:
        del pets[ID]
        print(f"Запись с ID {ID} успешно удалена из базы данных.\n")

command = ""
while command != "stop":
    print("Доступные команды: create, read, update, delete, list, stop")
    command = input("Введите команду: "). lower().strip()

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    elif command == "list":
        pets_list()
    elif command == "stop":
        print("Программа завершена. До свидания!")
    else:
        print("Неизвестная команда! Попробуйте ещё раз.\n")

