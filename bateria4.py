# Exercici1:
num = int(input("Fica un numero:"))
for i in range(1,num+1):
    if num % i == 0:
        print(i)

# Exercici2:
resultat = 0
suma_numeros = 0
quantitat_numeros = 0
while True:
    num = int(input("Digues un numero:"))
    if num ==0:
        break
    quantitat_numeros +=1
    suma_numeros += num
resultat = suma_numeros / quantitat_numeros
print(resultat)

# Exercici3:
num = int(input("Fica un numero:"))
resultat = 0
for i in range(1, numero + 1, 2):
print(resultat)
