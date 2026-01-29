try:
    A = int(input('Digite A: '))
    B = int(input('Digite B: '))
    R = A / B
    print(R)
except ZeroDivisionError:
    print('O valor de B não pode ser zero')
except ValueError:
    print('Digite números inteiros para A e B')
except:
    print('Não é possivel calcular a divisão')
print('Fim do programa')