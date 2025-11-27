# Diffie-Hellman
priem = int(input("Kies een priemgetal"));
grond = int(input("Kies een grondgetal"));

geheim = 15; # Dit is een geheim getal. Niemand mag het weten!
bericht = grond ** geheim;

print(f'bericht: {bericht} -> {bericht % priem}');

ontvangen_bericht = int(input("Wat is het resultaat dat de ander heeft gegeven?"));
sleutel = (ontvangen_bericht ** geheim) % priem;
print(f'sleutel = {sleutel}');
