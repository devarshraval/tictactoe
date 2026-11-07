import random

spaces = [1,2,3,4,5,6,7,8,9]
x = list()
o = list()

def grid():
    print()
    print(spaces[0], " | ", spaces[1], " | ", spaces[2])
    print("-"*13)
    print(spaces[3], " | ", spaces[4], " | ", spaces[5])
    print("-"*13)
    print(spaces[6], " | ", spaces[7], " | ", spaces[8])
    print

def win(x,o):
    winlist = [[0,1,2], [3,4,5], [6,7,8], [0,3,6], [1,4,7], [2,5,8], [0,4,8], [2,4,6]]
    for i in winlist:
        if all(j in x for j in i):
            return 1
        elif all(j in o for j in i):
            return 2
    return 0

grid()
for turn in range(9):
    if turn%2==0:        
        while True:
            c = input("Enter your choice: ")
            if c.isdigit() and int(c) in spaces:
                choice = int(c)
                break
        spaces[choice-1]="x"
        x.append(choice-1)
        grid()
    else:
        while True:
            choice = random.choice([1,2,3,4,5,6,7,8,9])
            if choice in spaces:
                spaces[choice-1]="o"
                o.append(choice-1)
                grid()
                break

    if win(x,o)==1:
        print("you win!")
        break
    elif win(x,o)==2:
        print("computer wins!")
        break

if win(x,o) not in [1,2]:
    print("draw!")
  
    



