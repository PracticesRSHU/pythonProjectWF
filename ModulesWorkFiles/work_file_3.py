#Hello World
def Work():
    with open('text.py', 'r') as f1, open('text.txt', 'w') as f2:
        for line in f1:
            f2.write(line[::-1])
    print("Work work")