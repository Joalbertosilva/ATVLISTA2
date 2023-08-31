dado = []
final = []
i = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: ')))
    cont = str((input('Voce deseja continuar [S/N]? ')))
    final.append(dado[:])
    dado.clear()
    if cont.lower() == 'n':
        break;
    
print(final)

