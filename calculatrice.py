print("")
print("      CALCULATRICE PYTHON")
print("")

while True:
    print("\nChoisissez une opération :")
    print("1 - Addition")
    print("2 - Soustraction")
    print("3 - Multiplication")
    print("4 - Division")
    print("5 - Quitter")

    choix = input("Votre choix : ")

    if choix == "5":
        print("Merci d'avoir utilisé la calculatrice !")
        break

    if choix not in ["1", "2", "3", "4"]:
        print("Choix invalide.")
        continue

    try:
        nombre1 = float(input("Entrez le premier nombre : "))
        nombre2 = float(input("Entrez le deuxième nombre : "))

        if choix == "1":
            resultat = nombre1 + nombre2
            symbole = "+"

        elif choix == "2":
            resultat = nombre1 - nombre2
            symbole = "-"

        elif choix == "3":
            resultat = nombre1 * nombre2
            symbole = "×"

        elif choix == "4":
            if nombre2 == 0:
                print("Impossible de diviser par zéro.")
                continue

            resultat = nombre1 / nombre2
            symbole = "÷"

        print(f"\nRésultat : {nombre1} {symbole} {nombre2} = {resultat}")

    except ValueError:
        print("Veuillez entrer des nombres valides.")
