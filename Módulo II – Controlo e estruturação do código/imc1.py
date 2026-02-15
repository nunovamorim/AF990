#%% primeira abordagem
# (1) recolher informacao de input, (2) formatar output

altura = float(input('Introduza a sua altura em metros (m): '))
peso   = float(input('Introduza o seu peso em quilogramas (kg): '))

print('O Índice de Massa Corporal (IMC) é: ', round(peso / (altura * altura), 2))


#%% segunda abordagem

# (1) recolher informacao de input, (2) aplicar expressao, (3) formatar output,
# (4) aplicar condicoes e imprimir mensagem

altura = float(input('Introduza a sua altura em metros (m): '))
peso   = float(input('Introduza o seu peso em quilogramas (kg): '))

# expressao para o calculo do IMC
imc = peso/(altura**2) 

print('O seu IMC é {0} e o seu estado é: '.format(round(imc, 2)), end='')

# condicoes
if ( imc < 16):
   print('muito abaixo do peso ideal')

elif ( imc >= 16 and imc < 18.5):
   print('abaixo do pesso ideal')

elif ( imc >= 18.5 and imc < 25):
   print('saudável')

elif ( imc >= 25 and imc < 30):
   print('acima do peso ideal')

elif ( imc >=30):
   print('muito acima do peso ideal')


#%%
# terceira abordagem

'''
Programa Python para calcular o Índice de Massa Corporal (IMC) do utilizador
=======================================
O input consiste na introducao de dois valores:

(1) o peso atual do utilizador em quilogramas e
(2) a altura do utilizador em metros

O output indica o valor do IMC e o estado de saude.
=======================================
'''

print('CALCULADORA DO INDICE DE MASSA CORPORAL\n')

def IMC(altura, peso):
    imc = peso/(altura**2)
    return imc

# Gestao de erros e excepcoes no input

while True:
    try:
        altura = float(input('Introduza a sua altura em metros (m): '))
        break
    except ValueError:
        print('Introduza um valor numérico válido para a altura: ')
        
if altura <= 0:
    print('A sua altura nao poderá ser menor que 0')

while True:
    try:
        peso = float(input('Introduza o seu peso em quilogramas (kg): '))
        break
    except ValueError:
        print('Introduza um valor numérico válido para o peso: ')

if peso <= 0 or peso > 200:
    print('O seu peso nao poderá ser menor que 0 kg e maior que 200 kg')


# chamar a funcao IMC
imc = IMC(altura, peso)

# Mostra o resultado
print('\nO seu Índice de Massa Corporal é %.2f\n' %imc)

# Verificacao do estado de peso do utilizador
if imc <= 18.5:
    print('O seu peso está ABAIXO do peso ideal')
elif 18.5 <= imc <= 24.9:
    print('O seu peso está NORMAL')
elif 25 <= imc <= 29.9:
    print('O seu peso está ACIMA do peso ideal')
elif imc >= 30:
    print('O seu peso está MUITO ACIMA do peso ideal')
else:
    print('Certifique-se que introduziu valores correctos')

#%% quarta abordagem

print('CALCULADORA DO INDICE DE MASSA CORPORAL\n')

altura = float(input('Introduza a sua altura em metros (m): '))
peso   = float(input('Introduza o seu peso em quilogramas (kg): '))

def IMC(altura, peso):
    imc = peso/(altura**2)
    return imc

# Gestao de valores anormais de peso e altura
if altura <0:
    print ('Nao pode ter altura negativa.')
    raise Exception('exit') # com exit() faz kill ao kernel
if altura < 1:
    print ('Com uma altura de ' + str(altura) + ' metros deve ser uma crianca, esta calculadora é apenas para adultos!')
    raise Exception('exit')
if altura > 3:
    print ('Tem a certeza que introduziu um valor correto de ' + str(altura) + ' metros de altura?')
    raise Exception('exit')
if altura > 4:
    print ('A sua altura nao pode exceder os 3 metros.')
    raise Exception('exit')
if peso < 0:
    print ('O seu peso nao pode ser negativo.')
if peso  < 40:
    print ('Com um peso de ' + str(peso) + ' kg, deve ser uma crianca, esta calculadora é apenas para adultos!')
    raise Exception('exit')
if peso > 200:
    print ('Tem a certeza que introduziu um valor correto de ' + str(peso) + ' kg de peso?')
    raise Exception('exit')

# Chamar a funcao IMC
imc = IMC(altura, peso)

# Mostra o resultado
print('\nO seu Índice de Massa Corporal é %.2f\n' %imc)

# Verificacao do estado de peso do utilizador
if imc <= 18.5:
    print('O seu peso está ABAIXO do peso ideal')
elif 18.5 <= imc <= 24.9:
    print('O seu peso está NORMAL')
elif 25 <= imc <= 29.9:
    print('O seu peso está ACIMA do peso ideal')
elif imc >= 30:
    print('O seu peso está MUITO ACIMA do peso ideal')
else:
    print('Certifique-se que introduziu valores correctos')


#%%
# quinta abordagem

'''
Programa Python para calcular o Índice de Massa Corporal (IMC) do utilizador
=======================================
O input consiste na introducao de dois valores:

(1) o peso atual do utilizador em kilogramas e
(2) a altura do utilizador em metros

O output indica o valor do IMC e o estado de saude.
=======================================
'''

from extras.addons import IMC