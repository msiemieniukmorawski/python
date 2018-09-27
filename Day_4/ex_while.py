# pętla while wykonuje się dopóki warunek jest spełniony (jest prawdą,
# ma wartość True)

# przed wykonaniem pętli sprawdzany jest warunek - tu nie wykona się ani razu
while False:
    print('Nic')

# ta pętla nie będzie miała końca
while True:
    print('To by było za długie')
    break  # instrukcja przerywająca działanie pętli

counter = 10
while counter: # wartość 0 jest rzutowana na nieprawdę (False)
    print(counter)
    counter -= 1  # równoważne z counter = counter - 1
print('end')

# ta pętla mogła by być zapisana też
counter = 10
while counter != 0: # wartość 0 jest rzutowana na nieprawdę (False)
    print(counter)
    counter -= 1  # równoważne z counter = counter - 1
print('end')
