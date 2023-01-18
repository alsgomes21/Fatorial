numero = int(input('Digite um número para o cálculo fatorial: '))

contador = numero

fatorial = 1

while contador > 0:
    print('{} '.format(contador), end='')
    print(' x ' if contador > 1 else ' = ', end='')
    fatorial *= contador
    contador = contador - 1
print('{}'.format(fatorial))