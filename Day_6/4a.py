with open('tekst1.txt', 'r') as file1:
    with open('text7.txt', 'w') as _file2:
        for line in file1.readlines():
            _file2.write(line)
