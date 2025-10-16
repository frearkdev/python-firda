# Dit stukje code geeft 3 verschillende vragen aan de gebruiker: Het eerste getal in de som, een operator (+, -, * of /) en het tweede getal in de som.)

getal1 = int(input("Geef het eerste nummer van de rekensom: "))
op = input("Geef een operator (+, -, * of /): ")
getal2 = int(input("Geef het tweedenummer van de rekensom: "))


# Hier word result gedefinieerd als None
result = None

# Dit stukje checkt wat de gebruiker van het programma als operator opgegeven heeft (als het niet + is word het -, als het niet - is word het *, als het niet * is word het /, en rekent vervolgens de som uit)
if op == "+":
    result = getal1 + getal2
elif op == "-":
    result = getal1 - getal2
elif op == "*":
    result = getal1 * getal2
elif op == "/":
    # Hier word gekeken of het getal geen 0 is
    if getal2 != 0:
        result = getal1 / getal2
        # Als het getal 0 is, vertel de gebruiker dat hij/zij niet door 0 kan delen
    else:
        print("Je kan niet door 0 delen")
        # Als de gebruiker iets anders invult dan +, -, * of /, vertel de gebruiker dat de operator ongeldig is
else:
    print("Ongeldige operator")


# Dit stukje kijkt of het result geen None is (result blijft none bij het geval van een ongeldige operator of een deling door 0), als dat het geval is geeft de code de rekensom en het antwoord. 
if result is not None:
    print(f"Resultaat: {getal1} {op} {getal2}: {result}")



