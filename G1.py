import random
player = 0
botscore = 0
for i in range(1,6):
    player = input("[scissors / paper / rock ] :")
    bot = random.choice(['scissors', 'paper', 'rock'])
    print(f"round:{i} player:{player} code:{bot}")
    if player == bot:
        print("draw")
    elif player == 'scissors' and bot == 'paper':
        print("playerwin")
        player +=1
    elif player == 'scissors' and bot == 'rock':
        print("botwin")
        botscore +=1
    elif player == 'paper' and bot == 'rock':
        print("playerwin")
        player +=1 
    elif player == 'paper' and bot == 'scissors':
        print("botwin")
        botscore +=1
    elif player == 'rock' and bot == 'paper':
        print("botwin")
        botscore +=1
    elif player == 'rock' and bot == 'scissors':
        print("playerwin")
        player = player+1
print(f'socre[player:{player} bot:{botscore}]')
if player == botscore:
    print("-----draw-----")
elif player > botscore:
    print("-----playerwin-----")
elif player < botscore:
    print("-----botwin-----")