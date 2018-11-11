# Zaimplementuj szyfr Cezara: https://pl.wikipedia.org/wiki/Szyfr_Cezara.
# Funkcja powinna przyjmować string do zaszyfrowania oraz przesunięcie.
# Funkcja powinna również ignorować spację (nie szyfrować jej).
# UWAGA: żeby pobrać listę wszystkich znaków skorzystaj z modułu string

def cesar_cipher(message, k=5):
    message = message.lower()
    message_array = list(message)
    message_array_ascii = [0] * len(message_array)
    last_elem_ascii = 122
    first_elem_ascii = 96
    k = int(k)
    for ii, elem in enumerate(message_array):
        elem_ascci = ord(elem)
        print(elem_ascci)
        if(elem_ascci == 32):
            message_array_ascii[ii] = ''
        elif(elem_ascci + k > last_elem_ascii):
            elem_shift = elem_ascci + k
            elem_shift = elem_shift - last_elem_ascii
            message_array_ascii[ii] = chr(first_elem_ascii + elem_shift)
        else:
            message_array_ascii[ii] = chr(elem_ascci + k)

    # message_array_ascii.remove(32)
    message_shift = ''.join(message_array_ascii)
    print(message_shift)

# secret_message = "galowie atakuja"
# print(cesar_cipher(secret_message) == 'lfqtbnjfyfpzof')

# Utrudnienie 1: Funkcja ma nie szyfrować białych znaków.
# Utrudnienie 2: Wywołując moduł homework można zaszyforwać podany
# przez konsolę tekst.

message = input('podaj wiadomość do szyfrowania: ')
shift = input('podaj przesunięcie: ')

if shift.isnumeric():
    temperature_outside = int(shift)
else:
    print('nie podales liczby')
    exit()

cesar_cipher(message, shift)