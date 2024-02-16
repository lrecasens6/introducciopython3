# Exercici6:
autenticació = [
        "nom": "Amilcar",
        "nom": "Sila"
]

def autenticar():
nom = input("Introdueix el nom d'usuari:")

if nom == autenticació["nom"]:
        print("Benvingut al sistema, ", nom)
else:
        print("Error de nom.")

autenticar()

# Exercici7:
numero = float(input("Digues un número:"))

if numero < 100:
    print("El número es menor que 100.")
elif numero > 100:
    print("El número es major que 100.")
else:
    print("El número es igual a 100.")

# Exercici8:
num = int(input("Digues un número:"))
if numero % 2 == 0:
    print(numero, "és un número parell.")
else:
    print(numero, "és un número senar.")

# Exercici9:
nota = float(input("Introdueix la teva nota:"))
if nota >= 1 and nota <= 4:
    resultat = "Insuficient"
elif nota == 5:
    resultat = "Suficient"
elif nota == 6:
    resultat = "Bé"
elif nota >= 7 and nota <= 8:
    resultat = "Notable"
elif nota >= 9 and nota <= 10:
    resultat = "Excel·lent"
print("La teva nota és", nota, "i el resultat és:", resultat)

# Exercici10:
anys_programador = int(input("Quants anys portes treballant com a programador?"))
if anys_programador < 5:
    print("Ets un programador junior.")
else:
    print("No ets un programador junior.")
