import random
user = 0
botscore = 0
draw = 0
for i in range(1,6):
    player = input("[scissors / paper / rock ] :")
    bot = random.choice(['scissors', 'paper', 'rock'])
    print(f"round:{i} player:{player} code:{bot}")
    if player == bot:
        print("draw")
        draw +=1
    elif player == 'scissors' and bot == 'paper':
        print("playerwin")
        user +=1
    elif player == 'scissors' and bot == 'rock':
        print("botwin")
        botscore +=1
    elif player == 'paper' and bot == 'rock':
        print("playerwin")
        user +=1 
    elif player == 'paper' and bot == 'scissors':
        print("botwin")
        botscore +=1
    elif player == 'rock' and bot == 'paper':
        print("botwin")
        botscore +=1
    elif player == 'rock' and bot == 'scissors':
        print("playerwin")
        user +=1
print(f'socre[player:{user} bot:{botscore} draw:{draw}]')
if user == botscore:
    print("-----draw-----")
elif user > botscore:
    print("-----playerwin-----")
elif user < botscore:
    print("-----botwin-----")
