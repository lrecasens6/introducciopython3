#Activitat1
import random
print(random.randint(1,6))

#Activitat2
import random
def dau_6()
    dau_6 = int(input("Tirada de 6 cares?"))
    print(random.randint(1, 6))

dau_6()

#Activitat3
import random
def daus_6(num_daus):
    daus_6 = int(input("Quants daus ha de llançar?"))
    for daus_6 in range(num_daus):
    print(random.randint(1, 6))

#Activitat4
import random
def dau_x(1):
    cares_dau = int(input("De quantes cares son els daus?"))
    print(random.randint(1, cares_dau))

#Activitat5
import random
def daus_x(num_daus, num_cares):
    for _ in range(num_daus):
    print([random.randint(1, num_cares) for _ in range(num_daus)])
