import lines as lines


def tack5():
    def analyze_grades(file_name):
     with open(file_name, 'r') as f:
        lines = f.readlines()

    students = {}
    # Аналізуємо зміст файлу та обчислюємо середній бал кожного студента
    for line in lines:
        parts = line.strip().split()
        name = parts[0]
        grades = list(map(int, parts[1:]))
        avg_grade = sum(grades) / len(grades)
        students[name] = avg_grade

    # Відфільтровуємо список студентів, які мають середній бал більше 7
    filtered_students = [name.upper() for name, avg_grade in students.items() if avg_grade > 7]

    # Записуємо прописані прізвища в новий файл
    with open('filtered_names.txt', 'w') as f:
        for name in filtered_students:
            f.write(name + '\n')


def analyze_grades(param):
    pass


if __name__ == '__main__':
    analyze_grades('grades.txt.txt')