from fileinput import filename


def tack7(lines=None):
    def swap_first_last_words(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()

    swapped_lines = []
    for line in lines:
        words = line.strip().split()
        if len(words) >= 2:
            words[0], words[-1] = words[-1], words[0]
        swapped_line = ' '.join(words)
        swapped_lines.append(swapped_line)

    with open(filename, 'w') as file:
        file.writelines(swapped_lines)

# Приклад виклику функції:
def swap_first_last_words(param):
    pass


swap_first_last_words('input.txt')

