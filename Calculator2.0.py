import math

class Calculator:
    def __init__(self):
        self.operations = {
            "+": self.addition,
            "-": self.subtract,
            "*": self.multiply,
            "/": self.divide
        }

    def addition(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

    def multiply(self, num1, num2):
        return num1 * num2

    def divide(self, num1, num2):
        if num2 == 0:
            raise ValueError("Erreur : Le quotient ne doit pas être égal à zéro.")
        return num1 / num2

    def add_operation(self, symbol, function):
        self.operations[symbol] = function

    def calculate(self, num1, symbol, num2):
        if symbol not in self.operations:
            raise ValueError("Erreur : Le symbole n'est pas valide.")
        if not (isinstance(num1, (float, int)) and isinstance(num2, (float, int))):
            raise ValueError("Erreur : Les nombres doivent être numériques.")

        function = self.operations[symbol]
        try:
            resultat = function(num1, num2)
            return resultat
        except Exception as e:
            raise ValueError(f"Erreur lors du calcul : {str(e)}")

# Définition des fonctions pour les opérations mathématiques avancées
def exponentiation(num1, num2):
    return num1 ** num2

def logarithme(num1, num2):
    if num1 <= 0 or num2 <= 0:
        raise ValueError("Erreur : Les deux valeurs doivent être positives.")
    return math.log(num1, num2)

def racine_carre(num1):
    if num1 < 0:
        raise ValueError("Erreur : La racine carrée d'un nombre négatif n'est pas définie.")
    return math.sqrt(num1)

# Programme Principal
calculator = Calculator()
calculator.add_operation("^", exponentiation)
calculator.add_operation("sqrt", racine_carre)
calculator.add_operation("log", logarithme)

while True:
    print("Choisissez parmi les opérations +, -, /, *, sqrt (racine carrée), log (logarithme), ^ (exponentiation) : ")
    operation = input("Choisissez l'opération à effectuer (ou 'q' pour quitter) : ")

    if operation == "q":
        print("Au revoir")
        break

    if operation in ["sqrt", "log"]:
        try:
            num1 = float(input("Entrez le nombre : "))
            # N'oubliez pas de passer None comme deuxième argument à calculate
            resultat = calculator.calculate(num1, operation, None)
            print(f"Le résultat est {resultat}")
        except ValueError as e:
            print(f"Erreur : {str(e)}")

        else:
            try:
                num1 = float(input("Entrez le premier nombre : "))
                num2 = float(input("Entrez le deuxième nombre : "))
                resultat = calculator.calculate(num1, operation, num2)
                print(f"Le résultat est {resultat}")
            except ValueError as e:
                print(f"Erreur : {str(e)}")
    else:
        print("Opération invalide")



