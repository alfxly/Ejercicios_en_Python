"""Diseñe un programa que lea dos listas A y B de N elementos cada uno y
multiplique el primer elemento de A con el último elemento de B y luego el
segundo elemento de A por el antepenúltimo elemento de B y así
sucesivamente hasta llegar al final de todos los   elementos de A por el
primer elemento de B. El resultado de la multiplicación almacenarlo en la
lista C."""

A = list(range(1, 11))
B = list(range(10, 0, -1))  

C = []

for i in range(len(A)):
    resultado = A[i] * B[i]
    C.append(resultado)

print("resultados de la multiplicación: ")
print(C)
