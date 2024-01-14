import random

player = 10
playerlist = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
scissors = 0
paper = 0
rock = 0

while True:
    if playerlist[0] == "-":
        continue
    else:
        user = random.choice(['scissors', 'paper', 'rock'])
        playerlist[0] = user

    for i in range(1, 10):
        if playerlist[i] == "-":
            continue
        else:
            playerlist[i] = random.choice(['scissors', 'paper', 'rock'])

    for i in playerlist:
        if i == "scissors":
            scissors += 1
        elif i == "paper":
            paper += 1
        elif i == "rock":
            rock += 1

    if scissors > 0 and paper > 0 and rock > 0:
        scissors = 0
        paper = 0
        rock = 0
        print(playerlist)
        print(f"scissors={scissors} paper={paper} rock={rock} player={player}")
    elif scissors > 0 and paper > 0 and rock == 0:
        player = player - paper
        print(playerlist)
        print(f"scissors={scissors} paper={paper} rock={rock} player={player}")
        scissors = 0
        paper = 0
        rock = 0
        for i in range(len(playerlist)):
            if playerlist[i] == 'paper':
                playerlist[i] = "-"
    elif scissors > 0 and paper == 0 and rock > 0:
        player = player - scissors
        print(playerlist)
        print(f"scissors={scissors} paper={paper} rock={rock} player={player}")
        scissors = 0
        paper = 0
        rock = 0
        for i in range(len(playerlist)):
            if playerlist[i] == 'scissors':
                playerlist[i] = "-"
    elif scissors == 0 and paper > 0 and rock > 0:
        player = player - rock
        print(playerlist)
        print(f"scissors={scissors} paper={paper} rock={rock} player={player}")
        scissors = 0
        paper = 0
        rock = 0
        for i in range(len(playerlist)):
            if playerlist[i] == 'rock':
                playerlist[i] = "-"

    if player == 1:
        break
