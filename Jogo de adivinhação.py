print ("Bem vindo") #imprime a frase bem vindo para o usuario
g = input("Digite um numero: ") #Pede para o usuario entrar com um numero.
guess = int(g)#Converte a entrada em um numero inteiro.
if guess == 5: #verifica se o numero é igual a 5.
    print("Voce venceu!") #SE sim mostra na tela vc venceu.
else: #Se não for igual a 5 imprime Voce perdeu.
    print("Voce perdeu!")
print ("Fim do jogo!")
