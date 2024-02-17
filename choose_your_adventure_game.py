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
print("Welcome to Treasure Island Game: Choose Your Adventure!")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
while True:  # Loop to restart the game after it ends
  choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right": \n').lower()
  if choice1 == "right":
    choice2 = input('\nYou made a right choice, and you\'ve come to a lake.\nThere is an island in the middle of the lake. \nType "wait" to wait for a boat or type "swim" to swim across: \n').lower()
    if choice2 == "wait":
      choice3 = input("\nYou arrive at the island unharmed. \nThere is a house with 3 doors.\nOne red, one yellow, and one blue. Which color do you choose? \n").lower()
      if choice3 == "red":
        print("\nYou entered in a room full of fire. Game Over.")
      elif choice3 == "yellow":
        print("\nYou found the treasure! You Won!")
      elif choice3 == "blue":
        print("\nYou entered in 'the Matrix room'. Your game will be restarted...")
        print("\nWelcome to Treasure Island Game: Choose Your Adventure (again)!")
        print("Your mission (again) is to find the treasure.\n") 
        continue  # Restart the game by going to the beginning of the loop
      else:
        print("\nYou chose a door that doesn't exist. Game Over.")
    else:
      print("\nYou get attacked by an angry alligator. Game Over.")
  else:
    print("\nYou got captured by leftists and communists. Game Over.")
  break  # Exit the loop after the game ends