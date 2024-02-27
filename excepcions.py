#Exercici1
 try i except per evitar l'error de divisió per zero.

 num1 = input("Introdueix el primer nombre: ")
 num2 = input("Introdueix el segon nombre: ")
 try:
     resultat = int(num1) / int(num2)
     print("El resultat de la divisió és: ",resultat)
 except:
     print("Error els numeros no son correctes o el segon numero es un zero.")

#Exercici2 
 entrada = input("introdueix el num: ")
 try:
     salida = int(entrada)
     print(salida)
 except:
     print("Error de entrada")

#Exercici3
 num1 = input("digues un numero")
 num2 = input("digues un altre numro")
 try:
     resultat = float(num1) + float(num2)
     print(resultat)
 except:
     print("Error")

#Exercici4
 llista=[1,3,4,7,9]
 index=input("Quin element vols mostrar? ")
 try:
     print(llista[int(index)])
 except:
     print("Aquest element no hi és ")
