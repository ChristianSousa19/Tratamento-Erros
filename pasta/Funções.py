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
def leiafloat(msg):
    while True:
     try:
      n=float(input(msg))
     except(ValueError,TypeError):
      print("\033[31mError por favor digite um numero real válido\033[m")
      continue
     except(KeyboardInterrupt):
      print("\033[mUsuario preferiu não digitar esse numero\033[m")
      return 0
     else:
         return n
num=leiaint,leiafloat("Digite um valor")
print(f"Você digitou o valor {(num)}")
