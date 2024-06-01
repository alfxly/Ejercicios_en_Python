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
