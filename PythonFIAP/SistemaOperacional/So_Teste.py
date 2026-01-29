import getpass
#import platform
#from datetime import datetime

#print("Nome Maquina...........:", platform.node())
#print("Arquitetura............:", platform.architecture())
#print("Sistema Operacional....:", platform.system())
#print("Versão do SO...........:", platform.release())
#print("Processador............:", platform.processor())
#print("Versão do Python.......:", platform.python_version())
#print(datetime.now().hour)

usuario = getpass.getuser()
senha = getpass.getpass("Digite sua senha.....: ")

if usuario == 'anton' and senha == 'fersoan77':
    print('Bem-Vindo Antony!')
else:
    print('Você não tem acesso!')
