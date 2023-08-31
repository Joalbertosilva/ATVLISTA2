dado = {}
princ = []
while True:
    dado['Nome'] = (str(input('Insira seu nome: ')))
    print()
    if len(dado['Nome']) <= 3:
        print('Insira mais de 3 caracteres: ')
        break
    dado['Sexo'] = (str(input('Sexo [F/M]: ')))
    print()
    print('A idade deve estar no limite de 0 a 150')
    dado['Idade'] = (int(input('Idade: ')))
    k = dado['Idade']
    if k >= 150:
        print('A idade deve estar dentro do limite de 0 a 150. Faça novamente')
        break
    print()
    dado['Salario'] = (int(input('Salario: ')))
    print()
    dado['Estado civil'] = (str(input('Estado civil [C/S/V/D]: ')))
    print()
    princ.append(dado.copy()) 
    dado.clear()
    cont = input('Voce deseja continuar [S/N]? ')
    if cont.lower() == 'n':
        break

print(princ)


