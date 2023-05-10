#Iordan File
#Add file
def tack1():
 import random

numbers = [random.randint(1, 100) for _ in range(10)]

with open('numbers.txt', 'w') as f:
    for number in numbers:
        f.write(str(number) + '\n')

with open('numbers.txt', 'r') as f:
    numbers = [int(line.strip()) for line in f]

numbers.sort()

with open('numbers.txt', 'w') as f:
    for number in numbers:
        f.write(str(number) + '\n')