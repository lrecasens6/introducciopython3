while True:
    print("Menú principal")
    print("Benvinguts a calc.py! Introdueix un numero de les seguents opcions:")
    print("0. Sortir")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    

    opcio = int(input("Introdueix un numero de les seguents opcions:"))

    if opcio == 0:
        print("Chao chao chao")
        break
    elif opcio in [1, 2, 3, 4]:
        num1 = float(input("Introdueix el primer numero"))
        num2 = float(input("Introdueix el segon numero"))

        if opcio == 1:
            suma = num1 + num2
            print("La resta de", num1, "+", num2, "es:", suma)
        if opcio == 2:
            resta = num1 - num2
            print("La resta de", num1, "-", num2, "es:", resta)
        if opcio == 3:
            multiplicacion = num1 * num2
            print("La multiplicació de", num1, "*", num2, "és:", multiplicacion)
        if opcio == 4:
            if num2 != 0:
                division = num1 / num2
                print("La divisió de", num1, "/", num2, "és:", division)
            else:
                print("La divisio de 0 es: Infinit")
        else:
            print("Opció no vàlida. Si us plau, introduïu una opció vàlida.")
      
