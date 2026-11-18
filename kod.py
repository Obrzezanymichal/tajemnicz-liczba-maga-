import random

secret_number = random.randint(0, 100)

print("""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

zgadnijliczbe = int(input("Wprowadz swoja odpowiedz: "))

while zgadnijliczbe != secret_number:
    print("Ha ha! Utknąłeś w mojej pętli!")

    if zgadnijliczbe < secret_number:
        print("Moja liczba jest większa")
    else:
        print("Moja liczba jest mniejsza")

    zgadnijliczbe = int(input("Try again: "))

print(zgadnijliczbe)
print("Brawo mugolu! Jesteś teraz wolny")
