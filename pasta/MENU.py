import time
import pasta
import arquivo

arq="curosemvideo.txt"
if arquivo.arquivoexiste(arq):
    print("Arquivo encontrado com sucesso!!!")
else:
    print("Arquivo não encontrado")
    pasta.criararquivo(arq)

while True:
 r=pasta.menu(['Ver pessoas cadastradas','Cadastrar nova pessoa','Sair do sistema'])
 if r ==1:
     print("opçao1")
     pasta.lerarquivo(arq)
 elif r==2:
     print("opção2")
     pasta.cabeça("Novo Cadastro")
     nome=str(input("Digite seu nome: "))
     idade=pasta.leiaint("Digite sua idade: ")
     pasta.cadastrar(arq,nome,idade)
 elif r==3:
     print("Saindo do sistema.....")
     time.sleep(1)
     break
 else:
     print("\033[31mError digite uma opção válida\033[m")
     time.sleep(2)


