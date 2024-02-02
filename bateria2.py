# Exercici1:
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

# Exercici2:
numero = float(input("Digues un número:"))

if numero < 100:
    print("El número es menor que 100.")
elif numero > 100:
    print("El número es major que 100.")
else:
    print("El número es igual a 100.")


