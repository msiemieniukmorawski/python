from Day_11.ex_privacy.pracownik import Pracownik

prac1 = Pracownik("John", "Travolta", 50000)
print(prac1)

prac2 = Pracownik("John", "Turturo", 30000)
print(prac2)

# obiekt.__dict__ - tutaj jest słownik zawierający zmienne oraz ich wartości

print("Dict prac1:")
print(prac1.__dict__)

print("\nDict prac2")
print(prac2.__dict__)

print("\nDict klasa")
print(Pracownik.__dict__)

prac1.roczna_podwyzka = 15

print("Dict prac1:")
print(prac1.__dict__)

print("\nDict prac2")
print(prac2.__dict__)

print("\nDict klasa")
print(Pracownik.__dict__)
