from contextlib import contextmanager


@contextmanager
def open_file(file_name, mode):
    f = open(file_name, mode)
    try:
        yield f
    finally:
        f.close()


with open_file('test_2.txt', 'w') as f:
    f.write('Testing 2\n')

print(f.closed)

try:
    with open_file('test_2.txt', 'w') as f:
        raise Exception
        f.write('Testing 3\n')
except:
    pass

print(f.closed)