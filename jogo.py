import random
print("#########################")
print("#  jogo de adivinhação  #")
print("#        ✨amanda✨     #")
print("#########################")
print("            ✨           ")

numerossecreto= random.randrange(0,100)
totaltentativas = 0 
ponto = 100

print("qual niveis de dificuldade?")
print("(1)-fácil (2)-médio (3)-difícil  ")

nivel = int(input("escolha um nível "))

if(nivel == 1 ):
    print("20 tentativas")
    totaltentativas = 20
elif(nivel == 2):
    prin


