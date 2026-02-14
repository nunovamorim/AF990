import argparse

# 1. Inicializar parser
parser = argparse.ArgumentParser(prog='teste',
								 #usage='%(prog)s [options] path',
								 #allow_abbrev=False,
                                 add_help=False,
								 description='Descricao da aplicacao',
								 epilog='--- Frase final do programa! ---')


#%%
# 2. Adicionar argumentos posicional obrigatorios (tipo, condicoes, help)
parser.add_argument('pos_arg', type=int,
                    help='Argumento de inteiro posicional obrigatorio')


# Argumento posicional opcional
parser.add_argument('opt_pos_arg', type=int, nargs='?',
                    help='Argumento de inteiro posicional opcional')


#%%
# Argumentos opcionais
parser.add_argument('--opt_arg', type=int,
                    help='Argumento de inteiro opcional')

parser.add_argument('--input', action='store', type=int, required=True)

parser.add_argument('--id', action='store', type=float)


#%%
# Traducao para portugues
parser.add_argument('-v', '--version', action='version',
                    version='%(prog)s 1.0',
                    help="Mostra o numero da versao do programa.")

parser.add_argument('-h', '--help', action='help', default=argparse.SUPPRESS,
                    help='Mostra esta mensagem de ajuda.')

parser._positionals.title = 'Argumentos obrigatorios'
parser._optionals.title   = 'Argumentos opcionais'


#%%
# 3. Parse dos argumentos
args = parser.parse_args()


#%% 
# 4. Accesso às variaveis
print("Valores dos argumentos:")
print(args.pos_arg)
print(args.opt_pos_arg)
print(args.input)


#%% 
# 5. Verificacao dos valores introduzidos
if args.pos_arg > 10:
    parser.error("pos_arg nao pode ser superior a 10")
