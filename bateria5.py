#Exercici19
resultat = 0
llista = []
while True:
    valor = input("Digues un numero:")
    if valor == "final":
        break
    else:
        llista.append(int(valor))
for numero in llista:
    resultat = resultat + numero
print("La suma del elements de la llista és:", resultat)
#Exercici20
def trobar_maxim_minim():
    numeros = []
    
    while True:
        valor = input("Introdueix un nombre enter (o 'final' per acabar): ")
        
        if valor.lower() == 'final':
            break
        
        try:
            numero = int(valor)
            numeros.append(numero)
        except ValueError:
            print("Si us plau, introdueix només nombres enters o 'final'.")

    if numeros:
        maxim = max(numeros)
        minim = min(numeros)
        suma = sum(numeros)
        print("El valor màxim és:", maxim)
        print("El valor mínim és:", minim)
        print("La suma dels números introduïts és:", suma)
    else:
        print("No s'han introduït números.")

if __name__ == "__main__":
    trobar_maxim_minim()

#Exercici21

#Exercici22
