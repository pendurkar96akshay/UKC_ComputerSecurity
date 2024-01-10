from itertools import product
import hashlib

salt = '5UA@/Mw^%He]SBaU'

values = ['laplusbelle', 'Marie', 'Curie', 'Woof', 'UKC', 'University', 'Kent', 'Canterbury', 'Jean',
          'Neoskour', 'Jvaist', 'Fairecourir', 'Eltrofor', '29', '12', '81', '80', 'December', '1981', '2', 'January', '1' ,'1980']

wordlist = ['']

# Combinations of all values without considering order
for combination in product(values, repeat=5):
    wordlist.append(''.join(combination))

for i in wordlist:
    final_string = i + salt
    hashedtext = hashlib.sha256(final_string.encode()).hexdigest()
    if hashedtext == '3281e6de7fa3c6fd6d6c8098347aeb06bd35b0f74b96f173c7b2d28135e14d45':
        print("HASH Matched! Password is - " + i)
        break