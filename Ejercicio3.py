"""Escribir un programa que almacene los números de 1 a 50, los muestre y

posteriormente elimine los números que no son primos y muestre los
números primos (un número natural mayor que 1 que tiene únicamente dos
divisores positivos distintos: él mismo y el 1)"""

def numeros_primos(lista):
    primos = []
    no_primos = []

    for num in lista:
        es_primo = 1
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    es_primo = 0
                    break
        else:
            es_primo = 0

        if es_primo == 1:
            primos.append(num)
        else:
            no_primos.append(num)

    print('Números primos:', primos)
    print('Números no primos:', no_primos)

lista = list(range(1, 51))
numeros_primos(lista)
