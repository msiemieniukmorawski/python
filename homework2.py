# Napisz program, który doradzi czy masz dzisiaj założyć kurtkę (bardzo na czasie).
# Powinien pobierać od użytkownika co najmniej trzy parametry: bieżącą temperaturę, stan opadów
# (brak, małe, duże, śnieg), wiatr (brak, mały, duży, huragan). Możesz zmodyfikować jakie wartości będzie mógł podawać użytkownik.

# Stwórz algorytm na podstawie własnych preferencji pogodowych z użyciem if, elif, else i operatorów logicznych.

# Program powinien co najmniej wyświetlać czy należy założyć kurtkę, ale może doradzać też w innych sprawach życiowych.
# Pamiętaj do stosowania się do zasad PEP8.

temperature_outside = input('Jaka jest temperatura na (temp w stopniach): ')
rain = input('Stan opadów (brak, małe, duże, śnieg): ')
wind = input('Wiart (brak, mały, duży, huragan): ')
rain_value = ['brak', 'małe', 'duże', 'śnieg']
wind_value = ['brak', 'małe', 'duży', 'huragan']
rain_jacket = ['małe', 'duże', 'śnieg']
wind_jacket = ['duży', 'huragan']
temperature_jacket = 20
error_mesage = 'załóż kurtkę'
if temperature_outside.isnumeric():
    temperature_outside = int(temperature_outside)
else:
    print('nie podales liczby')
    exit()

if rain not in rain_value:
    print('podałeś złą wartość dla opadów')
    exit()

if wind not in wind_value:
    print('podałeś złą wartość dla wiatru')
    exit()

if temperature_outside <= temperature_jacket and rain in rain_jacket:
    print(error_mesage)
elif rain in rain_jacket:
    print(error_mesage)
elif wind_value in wind_jacket:
    print(error_mesage)
elif temperature_outside <= temperature_jacket:
    print(error_mesage)
else:
    print('nie bierz kurtki')


