valores = []
c = []
v = []

for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    print()
for c, v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor: {v}')
    maior_valor = max(valores)
    indice_maior_valor = valores.index(maior_valor)
    menor_valor = min(valores)
    indice_menor_valor = valores.index(menor_valor)
print()
print('O maior valor foi {} na posição: {}'.format(maior_valor, indice_maior_valor))
print('O menor valor foi {} na posição: {}'.format(menor_valor, indice_menor_valor))

    
