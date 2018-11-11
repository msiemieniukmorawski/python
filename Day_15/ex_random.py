import random

print(random.random() )                            # Random float:  0.0 <= x < 1.0

print(random.uniform(2.5, 10.0))                 # Random float:  2.5 <= x < 10.0

print(random.randrange(10))                     # Integer from 0 to 9 inclusive

print(random.randrange(0, 101, 2))                 # Even integer from 0 to 100 inclusive

print(random.choice(['win', 'lose', 'draw']))      # Single random element from a sequence

deck = 'ace two three four'.split()
print(deck)
random.shuffle(deck)                        # Shuffle a list
print(deck)

print(random.sample([10, 20, 30, 40, 50], k=4))    # Four samples without replacement

