# Entrada
id_F1, num_F1, val_F1 = map(float, input('Insira as informações da ferramenta: id_F1, num_F1, val_F1\n').split())
id_F2, num_F2, val_F2 = \
    map(float, input('Agora insira as informações da segunda ferramenta: id_F2, num_F2, val_F2\n').split())

# Processo
valor_pago = (num_F1 * val_F1) + (num_F2 * val_F2)

# Saída
print('VALOR A PAGAR: R$', str('%.2f'%valor_pago))
