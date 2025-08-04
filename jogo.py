import random
print("#########################")
print("#  jogo de adivinhação  #")
print("#        ✨amanda✨     #")
print("#########################")
print("            ✨           ")

numeroSecreto= random.randrange(0,100)
totaltentativas = 0 
ponto = 100

print("qual niveis de dificuldade?")
print("(1)-fácil (2)-médio (3)-difícil  ")

nivel = int(input("escolha um nível "))

if(nivel == 1 ):
    print("20 tentativas")
    totaltentativas = 20
elif(nivel == 2):
    print("10 tentativas")
elif(nivel == 3):
    print("5 tentativas")
    totaltentativas = 5

for rodada in range (1, totaltentativas +1):
    print("tentaviva {} de {}". format(rodada, totaltentativas))
    
    chute_str = input("digite um número ente 1 a 100: ")
    chute = int(chute_str)

    if(chute < 1 or > 100):
        print(" número invalido")
        continue


    acertou =chute == numeroSecreto
    maior = chute > numeroSecreto
    menor = chute < numeroSecreto


