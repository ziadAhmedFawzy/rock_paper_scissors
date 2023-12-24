import random

x = random.randrange(0, 3)
recent = ["rocket", "paper", "scissors"]

while True:
    hand = input("rocket, paper, scissors : ")
    if recent[x] == "rocket" and hand == "paper":
        print(f"{recent[x]} -- {hand} : win\n")
    elif recent[x] == "paper" and hand == "scissors":
        print(f"{recent[x]} -- {hand} : win\n")
    elif recent[x] == "scissors" and hand == "rocket":
        print(f"{recent[x]} -- {hand} : win\n")
    elif recent[x] == hand:
        print(f"{recent[x]} == {hand} : draw\n")
        continue
    else:
        print(f"{recent[x]} -- {hand} : lose\n")
        break
