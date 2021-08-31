# Entrada
x: float = float(input('Insira o primeiro valor: '))
y: float = float(input('Insira o segundo valor: '))
z: float = float(input('Insira o terceiro valor: '))

# Processo
m = (x * 2 + y * 3 + z * 5) / 10
str("%1.f" % m)

# Saída
print("Média = ", m)
