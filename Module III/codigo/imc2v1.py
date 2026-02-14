'''
Programa Python para calcular o Índice de Massa Corporal (IMC) do utilizador
=======================================
O input consiste na introducao de:

(1) primeiro nome do utilizador
(2) ultimo nome do utilizador
(3) o peso atual do utilizador em quilogramas e
(3) a altura do utilizador em metros

O output indica o valor do IMC e o estado de saude.
=======================================
'''
from extras.addons import IMC, IMCI

print('\nCALCULADORA DO INDICE DE MASSA CORPORAL')

# input e verificacao

while True:
    pnome = input("Primeiro nome: ").lower()
    if pnome.isalpha():
        break
    print ("nome ivalido")

while True:
    unome = input("Ultimo nome: ").lower()
    if unome.isalpha():
        break
    print ("nome ivalido")

while True:
    try:
        altura = float(input('Altura (m): '))
        break
    except ValueError:
        print('valor invalido: ')
        
if altura <= 0:
    print('valor > 0')

while True:
    try:
        peso = float(input('Peso (kg): '))
        break
    except ValueError:
        print('valor invalido: ')

if peso <= 0 or peso > 200:
    print('0 < valor < 200')


# funcoes IMC e IMCI
imc  = IMC(altura, peso)
imci = IMCI(altura, peso)

# resultado formatado
print('\nIMC: %.2f \nIMCI: %.2f \nEstado: ' %(imc, imci), end='')


# classificacao
if imc <= 18.5:             print('MAGRO')
elif 18.5 <= imc <= 24.9:   print('NORMAL')
elif 25 <= imc <= 29.9:     print('FORTE')
elif imc >= 30:             print('OBESO')
else: print('Certifique-se que introduziu valores correctos')