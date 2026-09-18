pets = {}
name = input("Введите имя питомца: ")
kind = input("Введите вид питомца: ")
age = int(input("Введите возраст питомца: "))
owner = input("Введите имя хозяина: ")
pets[name] = {
    'Вид питомца': kind,
    'Возраст питомца': age,
    'Имя хозяина': owner
}
last_digit = age % 10
last_two_digits = age % 100
if 11 <= last_two_digits <= 14:
    age_string = "лет"
elif last_digit == 1: 
    age_string = "год"
elif 2 <= last_digit <= 4:
    age_string = "года"
else:
    age_string = "лет"
pet_name = list(pets.keys())[0]
inner_dict = list(pets.values())[0]
pet_kind = inner_dict['Вид питомца']
pet_age = inner_dict['Возраст питомца']
pet_owner = inner_dict['Имя хозяина']
print(f'Это {pet_kind} по кличке "{pet_name}". Возраст питомца: {pet_age} {age_string}. Имя хозяина: {pet_owner} ')
