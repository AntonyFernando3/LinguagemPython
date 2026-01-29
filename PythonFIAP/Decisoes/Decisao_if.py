nome=input("Digite o nome: ")
idade=int(input("Digite a Idade: "))
if idade >= 65:
    print("O paciente " + nome + " POSSUI atendimento prioritário!")
else:
    print("O paciente " + nome + " NÃO possui atendimento prioritário!")
print("FIM")