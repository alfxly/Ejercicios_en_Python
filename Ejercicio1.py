def calcular_salario(horas):
    if horas <= 40:
        salario = horas * 10000
    else:
        salario = (40 * 10000) + ((horas - 40) * 25000)
    return salario

salario_obrero = calcular_salario(45)
print("El salario del obrero es: $" + str(salario_obrero))
