# Entrada
# x é a base, y pode ser o lado e x é altura
x, y, z = map(float, input('Insira x, y e z:\n').split())

# Processo
Triangulo = (x * y) / 2.0
Circulo = 3.14159 * z ** 2
Trapezio = ((x + y) * z) / 2.0
Quadrado = y ** 2
Retangulo = x * y
# Pode-se utilizar por exemplo: y * y ou então y ** 2!

# Saída
print('Triangulo: ', str('%.3f'%Triangulo))
print('Circulo: ', str('%.3f'%Circulo))
print('Trapezio: ', str('%.3f'%Trapezio))
print('Quadrado: ', str('%3.f'%Quadrado))
print('Retangulo: ', str('%3.f'%Retangulo))
# Essa fórmula com o str é para indicar quantas casas decimais vai aparecer no resultado.
