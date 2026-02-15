#%% input fuction - input()

s = input()
s

name = input('Qual é o seu nome? ')
name

x = input('Introduza o seu nome: ')
print('Olá, ' + x) 

n = input('Introduza um número: ')
print(n + 100)

n = int(input('Introduza um número: '))
print(n + 100)


#%% funcao input com evaluation

x = input("Introduza um número: ") #10+10
print(x)
print(type(x))

y = eval(input("Introduza um número: ")) #10+10
print(y)
print(type(y))


#%% funcao de output - print()

print()
print("Olá planeta Terra!")
print("Qual é a sua resposta?", 42)

# criacao de strings
"Uso de aspas duplas"

'Uso de aspas simples'

"""Usar aspas triplas
para multiplas 
linhas"""


#%% Escape sequences

print("Primeira linha \nSegunda linha \n\tTerceira linha com tab")
print("Inserir aspas em strings \" or \' ")
print("No caso de querer backslash? \\ ")

#%% Formatacao de strings

first = 'David'
last = 'Bowie'
age = 69

message = "Olá " + "Mundo!"
message = 'O meu nome é {1}, {0} {1}'.format('David', 'Bowie')
message = f'Tenho {age} anos de idade.'

message = 'Caro sr. %s, seja bem vindo.' % last

print(message)
print('O meu nome é %s, ou melhor, %s %s' % (last, first, last))
print('O David Bowie faleceu com %d anos de idade.' % age)

import math
print('pi: %f \nshort pi %0.2f' % (math.pi, math.pi))

message = f'Caro sr. {last}, seja bem vindo.'
print(message)

print(f'O nome é {last}, {first} {last}.')
print(f"A idade de Bowie a multiplicar por pi é {age*math.pi}")
print(f"A idade de Bowie a multiplicar por pi é {age*math.pi:.2f}")


#%% separacao de characters

print('Existem', 6, 'membros dos Monty Python')

message = 'Existem' + 6 + 'membros dos Monty Python' # expressao errada
message = 'Existem' + str(6) + 'membros dos Monty Python'

print(message)

print('Existem', 6, 'membros dos Monty Python', sep=' ')
print('Existem', 6, 'membros dos Monty Python', sep=None)
print('Existem', 6, 'membros dos Monty Python', sep='\n')


#%% tratamento de erros e excepcoes

(x,y) = (5,0)
try:
    z = x/y
except ZeroDivisionError:
    print ("divisao por zero")

# loop try except
while True:
    try:
        n = input("Introduza um numero inteiro: ")
        n = int(n)
        break
    except ValueError:
        print("Inteiro nao valido! Tente novamente ...")
print("Excelente, introduziu um numero inteiro com sucesso!")

# try except except and finally
try:
    x = float(input("Introduza um numero: "))
    inverse = 1.0 / x
except ValueError:
    print("Deveria ter introduzido um int ou float")
except ZeroDivisionError:
    print("Infinito")
finally:
    print("Poderá levantar, ou nao, uma excepcao.")

# controlo de erros com if, elif, else
def myfunc(x=None):
   result = ""
   if x is None:
       result = "Nenhum argumento dado"
   elif x == 0:
       result = "Zero"
   elif 0 < x <= 3:
       result = "x está entre 0 e 3"
   else:
       result = "x é maior que 3"
   return result

