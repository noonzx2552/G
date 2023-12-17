import random
player = 10
while True:
    langelist = 0
    scissors = 0
    paper = 0
    rock = 0
    botlist = [0,0,0,0,0,0,0,0,0,0]
    #user = input("[scissors / paper / rock ] :")
    user = random.choice(['scissors', 'paper', 'rock'])
    botlist.append(user)
    for i in range(9):
        botlist[i] = random.choice(['scissors', 'paper', 'rock'])
    for i in botlist:
        if i == "scissors":
            scissors += 1
        elif i == "paper":
            paper += 1
        elif i == "rock":
            rock += 1
    if scissors >= 1 and paper >= 1 and rock >= 1:#draw
        player = player
        print(botlist)
        print(f'scissorss:{scissors} paper:{paper} rock:{rock}')
        print(f"player:{player}")
    elif scissors == 0 and paper >= 1 and rock >= 1:#paperwin
        player = player-rock
        print(botlist)
        print(f'scissorss:{scissors} paper:{paper} rock:{rock}')
        print(f"player:{player}")
        for i in range(10):
            if botlist[i] == "rock":
                botlist[i] == "."
        print(f'player : {player}')
    elif scissors >= 1 and paper == 0 and rock >= 1:#rockwin
        player = player-scissors
        print(botlist)
        print(f'scissors:{scissors} paper:{paper} rock:{rock}')
        print(f"player:{player}")
        for i in range(10):
            if botlist[i] == "scissors":
                botlist[i] == '.'
        print(f'player : {player}')
    elif scissors >= 1 and paper >= 1 and rock == 0:#scissorswin
        player = player-paper
        print(botlist)
        print(f'scissorss:{scissors} paper:{paper} rock:{rock}')
        print(f"player:{player}")
        for i in range(10):
            if botlist[i] == "paper":
                botlist[i] = '.'
    if player == 1:
        break
