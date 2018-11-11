class OpenFile():
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        # return True


with OpenFile('test_1.txt', 'w') as f:
    f.write('Testing 1\n')

print(f.closed)

try:
    with OpenFile('test_2.txt', 'w') as f:
        raise Exception
        f.write('Testing 3\n')
except:
    pass

print(f.closed)

with OpenFile('test_3.txt', 'w') as f:
    raise Exception
    f.write('Testing 3\n')
print(f.closed)