from random import randint

numero = [randint(0,999), randint(0,999), randint(0,999), randint(0,999), randint(0,999)]

print(f'Numeros sorteados {sorted(numero)}')
print(f'O menor valor sorteado foi: {min(numero)}')
print(f'O maior valor sorteado foi: {max(numero)}')

soma = max(numero) + min(numero)

print(f'A soma dos dois é igual a: {soma}')

