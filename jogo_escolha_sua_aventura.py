print('''
*******************************************************************************
      |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
      |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
      |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo(a) ao Jogo da Ilha do Tesouro: Escolha a sua Aventura!")
print("A sua missão é achar o tesouro.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
while True:  # Loop to restart the game after it ends
  choice1 = input('Você está em uma encruzilhada. Para onde você quer ir? Escreve "esquerda" ou "direita": \n').lower()
  if choice1 == "direita":
    choice2 = input('\nVocê fez a escolha certa, e chegou à um lago.\nHá uma ilha no meio do lago. \nEscreva "esperar" para esperar pelo barco ou escreva "nadar" ir nadando: \n').lower()
    if choice2 == "esperar":
      choice3 = input("\nVocê chegou na ilha são e salvo. \nHá uma casa com 3 portas.\nUma vermelha, uma amarela, e uma azul. Qual cor você escolhe? \n").lower()
      if choice3 == "vermelha":
        print("\nVocê entrou em uma sala cheia de fogo e morreu. Você perdeu o jogo.")
      elif choice3 == "amaraela":
        print("\nVocê encontrou o tesouro! Você ganhou!")
      elif choice3 == "azul":
        print("\nVocê entrou em uma 'sala da Matrix'. O seu jogo será reiniciado...")
        print("\nBem-vindo(a) ao Jogo da Ilha do Tesouro: Escolha a sua Aventura (novamente)!")
        print("A sua missão é (novamente) achar o tesouro.\n") 
        continue  # Restart the game by going to the beginning of the loop
      else:
        print("\nVocê escolheu uma porta que não existe. Você perdeu.")
    else:
      print("\nVocê foi atacado por um jacaré furioso. Você perdeu.")
  else:
    print("\nVocê foi capturado por esquerdistas e comunistas. Você perdeu.")
  break  # Exit the loop after the game ends