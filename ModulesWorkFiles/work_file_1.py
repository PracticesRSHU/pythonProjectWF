#Iordan File
#Add file
import datetime
first_name_1 = input("Введіть ім'я першого клієнта: ")
last_name_1 = input("Введіть прізвище першого клієнта: ")
birthdate_1 = input("Введіть дату народження першого клієнта (у форматі рррр-мм-дд): ")
balance_1 = float(input("Введіть баланс рахунку першого клієнта в грн: "))
first_name_2 = input("Введіть ім'я другого клієнта: ")
last_name_2 = input("Введіть прізвище другого клієнта: ")
birthdate_2 = input("Введіть дату народження другого клієнта (у форматі рррр-мм-дд): ")
balance_2 = float(input("Введіть баланс рахунку другого клієнта в грн: "))
today = datetime.date.today()
birthdate_1 = datetime.datetime.strptime(birthdate_1, '%Y-%m-%d')
age_1 = today.year - birthdate_1.year - ((today.month, today.day) < (birthdate_1.month, birthdate_1.day))
birthdate_2 = datetime.datetime.strptime(birthdate_2, '%Y-%m-%d')
age_2 = today.year - birthdate_2.year - ((today.month, today.day) < (birthdate_2.month, birthdate_2.day))
usd_rate = 26.5
balance_usd_1 = round(balance_1 / usd_rate, 2)
balance_usd_2 = round(balance_2 / usd_rate, 2)
print(f"Клієнт 1: {last_name_1} {first_name_1}, {age_1} років, баланс рахунку: ${balance_usd_1}")
print(f"Клієнт 2: {last_name_2} {first_name_2}, {age_2} років, баланс рахунку: ${balance_usd_2}")