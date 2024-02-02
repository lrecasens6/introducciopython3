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
a = 100
if a < 100:
        print("El numero és menor que 100.")
elif a ==100:
        print("El numero és igual que 100.")
else:
        print("El numero és major que 100.")
