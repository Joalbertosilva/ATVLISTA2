#dados = list()
#dados.append('Pedro')
#dados.append(18)

#dados2 = list()
#dados2.append('Joao')
#dados2.append(22)
#pessoas = list()
#pessoas.append(dados[:])
#pessoas.append(dados2[:]) 
#print(pessoas)
#print(pessoas[0][1])
#print(pessoas[1][0])
#print()
#print()

#dados3 = [['João' , 21] , ['Maria' , 19] , ['fernando' , 25]]
#for i in dados3:
#    print(f'{i[0]} tem {i[1]} anos de idade')

galera = list()
dado = list()
totmai = 0
totmen = 0
for cont in range(0, 4):
    dado.append(str(input('Digite seu nome: ')))
    dado.append(int(input('Digite sua idade: ')))
    galera.append(dado[:])
    dado.clear()

for i in galera:
    if i[1] >= 18:
        print(f'{i[0]} é maior de idade.')
        totmai += 1
        print()
    else:
        print(f'{i[0]} é menor de idade.')
        totmen += 1
        print()
print(f'Temos um total de {totmai} maior de idade e {totmen} menor de idade.') 