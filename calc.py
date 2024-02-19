while True:
    print("Menú principal")
    print("Benvinguts a calc.py! Introdueix un numero de les seguents opcions:")
    print("0. Sortir")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    break

    opcio = int(input("Introdueix un numero de les seguents opcions:"))
    if opcio == 0:
        print("Chao chao chao")
        break
    elif opcio in [1, 2, 3, 4]:
        num1 = float(input("Introdueix el primer numero"))
        num2 = float(input("Introdueix el segon numero"))

        if opcio == 1:
            suma = num1 + num2
            print("La suma del "num1" "+" "num2" es "suma" ")
