# Entrada
nome: input('Insira seu nome: ')
sl: float = float(input('Insira seu salário: '))
vendas: float = float(input('Insira o total de vendas: '))

# Processo
slf = sl + vendas*0.25
slf = str('%.2f'%slf)

# Saída
print('O salário total é: ', slf)