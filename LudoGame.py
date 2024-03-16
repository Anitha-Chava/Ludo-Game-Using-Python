print("WELCOME TO LUDO ONLINE GAME PLATFORM")
import random

def play():
    p1=input("Player 1, please enter your name:")
    p2=input("Player 2, please enter your name:")
    pc1=[]
    pc2=[]
    for i in range(0,4):
        pc1.append(0)
    for i in range(0,4):
        pc2.append(0)
    turn = 0
    end = 57
    
    while(1):
        if turn%2==0:
            print(p1," Your turn")
            
            dice = random.randint(1,6)
            print("Dice Showed : ",dice)
            if dice == 6:
                turn = 0
            else:
                turn = 1
            
            choice = int(input("Enter coin number 1,2,3,4:"))
            pc1[choice-1] = pc1[choice-1] + dice
            if (pc1[choice-1] == pc2[0] and (pc2[0] != 9 or pc2[0] != 22 or pc2[0] != 35 or pc2[0] != 48)):
                pc2[0] = 0
            elif (pc1[choice-1] == pc2[1] and (pc2[1] != 9 or pc2[1] != 22 or pc2[1] != 35 or pc2[1] != 48)):
                pc2[1] = 0
            elif (pc1[choice-1] == pc2[2] and (pc2[2] != 9 or pc2[2] != 22 or pc2[2] != 35 or pc2[2] != 48)):
                pc2[2] = 0
            elif (pc1[choice-1] == pc2[3] and (pc2[3] != 9 or pc2[3] != 22 or pc2[3] != 35 or pc2[3] != 48)):
                pc2[3] = 0
            for i in range(0,4):
                print(pc1[i])
            for i in range(0,4):
                if pc1[i]>=57 :
                    printf(i+1, "coin reached destination play with remaing coins")
            check = 0
            check = win(pc1)
            if check == 1:
                print(p1, "Congratulations..!, You win the game")
            
        else:
            print(p2," Your turn")
            
            dice = random.randint(1,6)
            print("Dice Showed : ",dice)
            if dice == 6:
                turn = 1
            else:
                turn = 0
            
            choice = int(input("Enter coin number 1,2,3,4:"))
            pc2[choice-1] = pc2[choice-1] + dice
            if (pc2[choice-1] == pc1[0] and (pc1[0] != 9 or pc1[0] != 22 or pc1[0] != 35 or pc1[0] != 48)):
                pc1[0] = 0
            elif (pc2[choice-1] == pc1[1] and (pc1[1] != 9 or pc1[1] != 22 or pc1[1] != 35 or pc1[1] != 48)):
                pc1[1] = 0
            elif (pc2[choice-1] == pc1[2] and (pc1[2] != 9 or pc1[2] != 22 or pc1[2] != 35 or pc1[2] != 48)):
                pc1[2] = 0
            elif (pc2[choice-1] == pc1[3] and (pc1[3] != 9 or pc1[3] != 22 or pc1[3] != 35 or pc1[3] != 48)):
                pc1[3] = 0
            for i in range(0,4):
                print(pc2[i])
            for i in range(0,4):
                if pc2[i]>=57 :
                    print(i+1, "coin reached destination play with remaing coins")
            check = 0
            check = win(pc2)
            if check == 1:
                print(p2, "Congratulations..!, You win the game")
def win(points_List):
    end = 57
    c=0
    for i in range(0,4):
        if points_List[i] >= end :
            c=c+1
    if c == 4:
        return 1
    else:
        return 0
    

play()
                
            
            
            
            
                
                
                
            
                    
    
    
    
