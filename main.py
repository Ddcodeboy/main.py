

import random
choices = ["R", "P", "S"]

computer = random.choice(choices)
player = input("R, P,or S: ").upper()

while player not in choices:
    print("error")
    player = input("Try another option: ").upper()
    continue

if player == computer:
  print("player(",player + " )")
  print("computer(", computer+" )")
  print("A tie")
elif player == "R":
    if computer == "P":
        print("player(", player + " )")
        print("computer(", computer+" )")
        print("player lose")
    if computer == "S":
         print("player(", player + " )")
         print("computer(", computer + " )")
         print("player win")
elif player == "S":
    if computer == "R":
        print("player(", player + " )")
        print("computer(", computer + " )")
        print("player lose")
    if computer == "P":
        print("player(", player + " )")
        print("computer(", computer + " )")
        print("player win")
elif player == "P":
    if computer == "S":
        print("player(", player + ")")
        print("computer(", computer + " )")
        print("player lose")
    if computer == "R":
        print("player(", player + " )")
        print("computer(", computer + " )")
        print("player win")


