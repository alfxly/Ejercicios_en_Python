"""En una empresa se requiere calcular el salario semanal de cada uno de los
n obreros
que laboran en ella. El salario se obtiene de la sig. forma: 
 Si el obrero trabaja 40 horas o menos se le paga $10.000 por hora 
 Si trabaja más de 40 horas se le paga $20.000 por cada una de las
primeras 40
horas y $25.000 por cada hora extra."""


def calcular_salario(horas):
    if horas <= 40:
        salario = horas * 10000
    else:
        salario = (40 * 10000) + ((horas - 40) * 25000)
    return salario

salario_obrero = calcular_salario(45)
print("El salario del obrero es: $" + str(salario_obrero))
