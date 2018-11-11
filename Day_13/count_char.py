import sys

print(sys.argv)

if len(sys.argv) != 3:
    print("Błędna liczba argumentów!")
    exit()

zdanie = sys.argv[1]
# zdanie = list(sys.argv[1])
litera = sys.argv[2]

assert isinstance(zdanie, str), 'Błędny pierwszy argument!'

print(zdanie.count(litera))
