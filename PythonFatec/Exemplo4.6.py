risco = input('Digite BX ou AL para grau de risco: ')
valor = float(input('Digite o valor: '))

if risco != 'BX' and risco != 'Al':
    print(f'{risco} é inválido para o grau de risco')
else:
    if risco == 'BX':
        if valor < 1000.0:
            tipo = 'Poupança'
        else:
            tipo = 'Renda Fixa'
    else:
        if valor < 1000.0:
            tipo = 'Bitcoins'
        else:
            tipo = 'Ações'
            print(f'Você deve investir em {tipo}')
