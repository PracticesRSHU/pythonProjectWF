
with open('file1.txt', 'r') as f1, open('file2.txt', 'w') as f2:
    f2.write(f1.read())


with open('file2.txt', 'r') as f2:
    print(f2.read())

import os
os.remove('file1.txt')
