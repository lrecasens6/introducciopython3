# Exercici1:
num = int(input("Digues un número: "))
print("Taula de multiplicar de", num, ":")
for i in range(1, 11):
    resultat = num * i
    print(num, "x", i, "=", resultat)

# Exercici2:
num = int(input("Digues un número: "))
suma = 0
for i in range(1, num + 1):
print("La suma dels números fins a", num, "és:", suma)

# Exercici3:
num = int(input("Introdueix un número: "))
suma = 0
for i in range(1, num + 1):
    if i % 2 == 0:  
print("La suma dels números parells fins a", num, "és:", suma)

#Exercici4:
num = int(input("Introdueix un número: "))
opcio = input("Vols sumar números parells o senars")
suma = 0
for i in range(1, num + 1):
    if opcio == "Parell" and i % 2 == 0: 
    elif opcio == "S" and i % 2 != 0:  # Comprova si l'opció és sumar senars i si i és senar

if opcio == "Parell":
    print("La suma dels números parells fins a", numero, "és:", suma)
elif opcio == "Senar":
    print("La suma dels números senars fins a", numero, "és:", suma)
else:
    print("Opció invàlida.")

#Exercici5:
def primer(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
