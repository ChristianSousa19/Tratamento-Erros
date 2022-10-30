import pasta


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