import pasta


def leiaint(msg):
    while True:
     try:
      n=int(input(msg))
     except(ValueError,TypeError):
      print("\033[31mError por favor digite um numero inteiro válido\033[m")
      continue
     except(KeyboardInterrupt):
      print("\033[mUsuario preferiu não digitar esse numero\033[m")
      return 0
     else:
         return n
def cabeça(msg):
    print('-' * 50)
    print(f'{msg}')
    print('-' * 50)
def linha(tam=42):
    return "=-"*tam
def menu(lista):
   pasta.cabeça("Menu principal")
   c=1
   for i in lista:
       print(f"\033[33m{c}\033[m-\033[34m{i}\033[m")
       c+=1
   print(linha())
   op=leiaint('\033[32mSua opção:\033[m ')
   return op
def arquivoexiste(nome):
    try:
        a=open(nome,'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
def criararquivo(nome):
    try:
        a=open(nome,'wt+')
        a.close()
    except:
        print("Houve um erro na criação do arquivo")
    else:
        print(f"Arquivo {nome} criado com sucesso")
def lerarquivo(nome):
    try:
        a=open(nome,"rt")
    except:
        print("Erro ao ler arquivo")
    else:
        pasta.cabeça("Pessoas cadastradas")
        print(a.read())
    finally:
        a.close()
def cadastrar(arq,nome="",idade=0):
    try:
        a=open(arq,"rt")
    except:
        print("Error ao ler arquivo")
    else:
        pasta.cabeça("Pessoas cadastradas com sucesso")
        print(a.read())
    try:
        a.write(f"{nome},{idade}")
    except:
     print("Houve um erro na hora de escrever os dados")
    else:
        print(f"Um novo regsitro de {nome} foi adcionado ")
    a.close()



