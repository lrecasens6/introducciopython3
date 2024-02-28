alçada = 10
amplada = 20
posicio_asterisc = 0
pos_y = 0
cadena_buida = "|"+ " " * amplada + "|"
cadena_border = "'" * (amplada+2)
while True:
    cadena_asterisc = " "
    for i range(amplada):
        if i == posicio_asterisc
            cadena_asterisc += "*"
        else:
            cadena_asterisc += " "
    cadena_asterisc += " "
    print(cadena_border)
    for i in range(alçada)
    print(' ' * posicio_asterisc + '*')

    direccio = input("Clica 'a' per moure a la esquerra, 'd' per moure a la dreta, 'w' per moure a dalt, 's' per moure a baix")
    if direccio == 'a' and posicio_asterisc > 0:
        posicio_asterisc -= 1
    elif direccio == 'd' and posicio_asterisc < amplada:
        posicio_asterisc += 1
    if direccio == 'w' and pos_y < alçada:
        pos_y += 1
    elif direccio == 's' and pos_y > 0:
        pos_y -= 1
