Nome = input('Digite o nome: ')
Peso = float(input('Digite o peso: '))
if Peso < 52:
    Categoria = ''
elif Peso < 65:
    Categoria = 'Pena'
elif Peso < 72:
    Categoria = 'Leve'
elif Peso < 79:
    Categoria = 'Ligeiro'
elif Peso < 86:
    Categoria = 'Meio-Médio'
elif Peso < 90:
    Categoria = 'Médio'
elif Peso < 100:
    categoria = 'Pesado'
    msg = 'O lutador {} pesa {:.3f} Kg e se enquadra na categoria {}'
if Categoria != '':

 print(msg.format(Nome, Peso, Categoria))
else:
    print(f'Peso inválido: {Peso}')
    print('Fim do programa')