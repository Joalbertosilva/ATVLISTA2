valores = []

print('*'*10)
print('Insira numeros apenas entre 0 e 1000!')
print('*'*10)
print()
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para a posição {c}: ')))
    print()
    if valores[c] >= 1000:
        print('Insira um valor entre 0 e 1000.')
        break
    print()
for c, v in enumerate(valores):
    if valores[c] >= 1000:
        break
    print()
    print(f'Na posição {c} encontrei o valor: {v}')
    maior_valor = max(valores)
    indice_maior_valor = valores.index(maior_valor)
    menor_valor = min(valores)
    indice_menor_valor = valores.index(menor_valor)
    soma = maior_valor + menor_valor
print()
print('O maior valor foi {} na posição: {}'.format(maior_valor, indice_maior_valor))
print('O menor valor foi {} na posição: {}'.format(menor_valor, indice_menor_valor))
print(f'A soma do maior e o menor é igual a: {soma}')

    
