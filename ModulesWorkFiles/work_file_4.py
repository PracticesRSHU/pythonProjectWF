#branch_Serhii
# Запитуємо в користувача ім'я файлу з текстом Python-програми
file_name = input("Введіть ім'я файлу з текстом Python-програми: ")
try:
# Відкриваємо файл у режимі читання
    with open(file_name, "r") as file:
# Зчитуємо весь текст з файлу
        text = file.read()
# Розділяємо текст на слова
        words = text.split()
# Проходимося по кожному слову і замінюємо малі символи на прописні,
# якщо довжина слова більше двох символів
        for i in range(len(words)):
            if len(words[i]) > 2:
                words[i] = words[i].upper()
# З'єднуємо слова знову в один рядок
        new_text = " ".join(words)
# Виводимо змінений текст на екран
        print(new_text)
except FileNotFoundError:
# Якщо файл не знайдено, виводимо повідомлення про помилку
    print("Файл не знайдено.")
#add file2023