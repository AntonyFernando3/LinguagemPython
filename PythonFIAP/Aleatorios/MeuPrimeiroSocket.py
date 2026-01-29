import socket

resp = "S"
while (resp == "S"):
    try:
        url = input("\n Digite uma url (ex: google.com): ")
        ip = socket.gethostbyname(url)
        print(f"O IP referente a url informada é: {ip}")
    except socket.gaierror:
        print("Erro: Não foi possível encontrar o IP para esta URL.")
    resp = input("Digite <s> para continuar: ").upper()

print("Programa encerrado.")




