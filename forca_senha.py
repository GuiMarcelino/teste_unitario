def numero_de_caracteres(senha):
    resultado = len(senha) * 4
    return resultado


def letras_maiusculas(senha):
    upper = 0
    for char in senha:
        if char.isupper():
            upper += 1
    calculo = ((len(senha) - upper) * 2)
    return calculo


def letras_minusculas(senha):
    lower = 0
    for char in senha:
        if char.islower():
            lower += 1
    calculo = ((len(senha) - lower) * 2)
    return calculo

