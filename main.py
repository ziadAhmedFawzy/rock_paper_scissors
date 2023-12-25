import random

x = random.randrange(0, 3)
recent = ["rock", "paper", "scissors"]

while True:
    hand = input("rock, paper, scissors : ")
    if recent[x] == "rock" and hand == "paper":
        print(f"{recent[x]} -- {hand} : win\n")
    elif recent[x] == "paper" and hand == "scissors":
        print(f"{recent[x]} -- {hand} : win\n")
    elif recent[x] == "scissors" and hand == "rock":
        print(f"{recent[x]} -- {hand} : win\n")
    elif recent[x] == hand:
        print(f"{recent[x]} == {hand} : draw\n")
        continue
    else:
        print(f"{recent[x]} -- {hand} : lose\n")
        break
