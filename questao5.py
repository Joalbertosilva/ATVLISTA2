primos = []
princi = []
while True:
    numero = int(input('Digite um numero: '))
    for i in range(1, numero + 1):
        if numero % i == 0:
            primos.append(i)
        else: 
            pass
    print(primos)
    if len(primos) == 2:
        print('é primo')
    else:
        print('não é primo')
    primos.clear()
    cont = input('Voce deseja continuar[S/N]? ')
    if cont.lower() == 'n':
        break
    
