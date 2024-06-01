A = list(range(1, 11))
B = list(range(10, 0, -1))  

C = []

for i in range(len(A)):
    resultado = A[i] * B[i]
    C.append(resultado)

print("resultados de la multiplicación: ")
print(C)
