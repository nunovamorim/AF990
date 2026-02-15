def IMC(altura, peso):
    '''expressao clasica de calculo do IMC'''
    imc = peso / (altura ** 2)
    return imc

def IMCI(altura, peso):
    '''expressao nova de calculo do IMC'''
    imc = 1.3 * (peso / (altura ** 2.5))
    return imc