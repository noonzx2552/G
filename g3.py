def scanX(chanal):
    x_list=[]
    for i in range(3):
        for j in range(3):
            if chanal[i][j] == "X":
                x_list.append(i)
                x_list.append(j)
    return x_list
def scanO(chanal):
    O_list=[]
    for i in range(3):
        for j in range(3):
            if chanal[i][j] == "O":
                O_list.append(i)
                O_list.append(j)
    return O_list
def checkwinX(chanal,status):
    X = 0
    for i in range(3):
        if chanal[0][i] == "X":
            X += 1
        if X == 3:
            status = "Xwin"
        else:
            X=0
    for i in range(3):
        if chanal[1][i] == "X":
            X += 1
        if X == 3:
            status = "Xwin"
        else:
            X=0
    for i in range(3):
        if chanal[2][i] == "X":
            X += 1
        if X == 3:
            status = "Xwin"
        else:
            X=0
    for i in range(3):
        if chanal[i][0] == "X":
            X += 1
        if X == 3:
            status = "Xwin"
        else:
            X=0
    for i in range(3):
        if chanal[i][1] == "X":
            X += 1
        if X == 3:
            status = "Xwin"
        else:
            X=0
    for i in range(3):
        if chanal[i][2] == "X":
            X += 1
        if X == 3:
            status = "Xwin"
        else:
            X=0
    for i in range(3):
        if chanal[0][0] == "X" and chanal[1][1] == "X" and chanal[2][2] == "X":
            status = "Xwin"
    return status
def checkwinO(chanal,status):
    X = 0
    for i in range(3):
        if chanal[0][i] == "O":
            X += 1
        if X == 3:
            status = "Owin"
        else:
            X=0
    for i in range(3):
        if chanal[1][i] == "O":
            X += 1
        if X == 3:
            status = "Owin"
        else:
            X=0
    for i in range(3):
        if chanal[2][i] == "O":
            X += 1
        if X == 3:
            status = "Owin"
        else:
            X=0
    for i in range(3):
        if chanal[i][0] == "O":
            X += 1
        if X == 3:
            status = "Owin"
        else:
            X=0
    for i in range(3):
        if chanal[i][1] == "X":
            X += 1
        if X == 3:
            status = "Xwin"
        else:
            X=0
    for i in range(3):
        if chanal[i][2] == "X":
            X += 1
        if X == 3:
            status = "Xwin"
        else:
            X=0
    for i in range(3):
        if chanal[0][0] == "X" and chanal[1][1] == "X" and chanal[2][2] == "X":
            status = "Xwin"
    return status

number_round = 1
status = "-"
x1 = 0
x2 = 0
chanal = [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
         ]
while True:
    while True:
        while True:
            x1 = int(input("row :"))
            if x1 <= 2:
                break
        while True:
            x2 = int(input("col :"))
            if x2 <= 2:
                break
        if chanal[x1][x2] == "-":
            break
    if number_round % 2 == 0:
        chanal[x1][x2] = "O"
    else:
        chanal[x1][x2] = "X"
    number_round += 1
    print(f"{chanal[0][0]}|{chanal[0][1]}|{chanal[0][2]}")
    print("_____")
    print(f"{chanal[1][0]}|{chanal[1][1]}|{chanal[1][2]}") 
    print("_____")
    print(f"{chanal[2][0]}|{chanal[2][1]}|{chanal[2][2]}")
