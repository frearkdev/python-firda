teller = 0
wachtwoord = "test"
for teller in range(10):
    teller += 1
    if input ('Geef wachtwoord ') == wachtwoord:
        break
    if teller > 3:
        print('Je mag geen wachtwoord invoeren')
        break