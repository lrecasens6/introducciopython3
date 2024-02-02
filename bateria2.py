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

