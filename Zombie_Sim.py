#------------------------------------------------------------------------------------------
#
# Title: Zombie Simulator
# Creator: Ashish Tamang
# Student of University of Waterloo
# Created: Winter 2012
#
#   Description:
#
#       'Zombie-Simulator' features a 10 by 10 grid which represents a bustling city
#       inhabited by humans. The program then runs an algorithm that predicts
#       what would happen to the city if a zombie outbreak were to occur. 
#
#       The program is divided into two parts:
#
#       Part A: 
#
#          The user is able to pick how many turns they would like to run the algorithm for.
#          An intial starting populace of humanity in the city is mapped out.
#          During Turn 0, a single zombie is spawned randomly in one of the grids in the city.
#          The program then outputs the final outcome after an n number of turns have passed.
#
#       Part B:
#
#          The user can choose to spawn an n number of zombies in a random location in the city.
#          The program runs the algorithm and determines the number of turns it took for either
#          humanity or the zombies to be completely wiped out.
#
#   Zombie Algorithm:
#
#       Every zombie alive, during a single turn, goes through this algorithm once.
#
#       The algorithm can sorted into three steps:
#               i) Movement: the zombie, in a randomized fashion, moves one block through the city.
#              ii) Encounter: if the zombie encounters a human iii) is initiated.
#                             if this does not occur, the zombie ends its turn.
#             iii) Result: The result of the encounter between a zombie and a human is
#                          determined randomly and can end in one of three way:
#                              1) the zombie is eliminated
#                              2) the human is eliminated
#                              3) the human is turned into a zombie
#
#   Instructions:
#
#        To use, simply run the run the program on PythonIDLE (as it has 
#        a larger screen for text to show up) and follow the instructions. 
#
#
#-------------------------------------------------------------------------------------------

import random
import sys
sys.setrecursionlimit(100000)
A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,J1,J2,J3,J4,J5,J6,J7,J8,J9,J10 = [0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
Grid ={(1,1):A1,(2,1):B1,(3,1):C1,(4,1):D1,(5,1):E1,(6,1):F1,(7,1):G1,(8,1):H1,(9,1):I1,(10,1):J1,(1,2):A2,(2,2):B2,(3,2):C2,(4,2):D2,(5,2):E2,(6,2):F2,(7,2):G2,(8,2):H2,(9,2):I2,(10,2):J2,(1,3):A3,(2,3):B3,(3,3):C3,(4,3):D3,(5,3):E3,(6,3):F3,(7,3):G3,(8,3):H3,(9,3):I3,(10,3):J3,(1,4):A4,(2,4):B4,(3,4):C4,(4,4):D4,(5,4):E4,(6,4):F4,(7,4):G4,(8,4):H4,(9,4):I4,(10,4):J4,(1,5):A5,(2,5):B5,(3,5):C5,(4,5):D5,(5,5):E5,(6,5):F5,(7,5):G5,(8,5):H5,(9,5):I5,(10,5):J5,(1,6):A6,(2,6):B6,(3,6):C6,(4,6):D6,(5,6):E6,(6,6):F6,(7,6):G6,(8,6):H6,(9,6):I6,(10,6):J6,(1,7):A7,(2,7):B7,(3,7):C7,(4,7):D7,(5,7):E7,(6,7):F7,(7,7):G7,(8,7):H7,(9,7):I7,(10,7):J7,(1,8):A8,(2,8):B8,(3,8):C8,(4,8):D8,(5,8):E8,(6,8):F8,(7,8):G8,(8,8):H8,(9,8):I8,(10,8):J8,(1,9):A9,(2,9):B9,(3,9):C9,(4,9):D9,(5,9):E9,(6,9):F9,(7,9):G9,(8,9):H9,(9,9):I9,(10,9):J9,(1,10):A10,(2,10):B10,(3,10):C10,(4,10):D10,(5,10):E10,(6,10):F10,(7,10):G10,(8,10):H10,(9,10):I10,(10,10):J10}

def MakingLists(Grid):                      
    n = 1
    for i in range(10):
        w = 1
        for i in range (10):
            meow = random.randrange(100)+1
            Grid[(n,w)][0]= meow
            w = w+1
        n = n+1
        
def BirthOfTheZombay(Grid):
    n = random.randrange(10)+1
    w = random.randrange(10)+1
    Grid[n,w][1] = 1
    
def DefineTheZombay(Grid):
    n = random.randrange(10)+1
    w = random.randrange(10)+1
    Grid[n,w][1] = input("\nHow many zombies would you like to spawn? --> ")
    while True:
        try:
            Grid[n,w][1] = int(Grid[n,w][1])
            break
        except ValueError:
            print ("Please enter a valid entry!")
    

def NekoMovement(Grid):
    if n == 1 and w == 1:
        Sanjelly = random.randrange(2)+1
        if Sanjelly == 1:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n+1,w][1] = Grid[n+1,w][1] + 1
        elif Sanjelly == 2:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w+1][1] = Grid[n,w+1][1] + 1
    elif n == 10 and w == 1:
        Sanjelly = random.randrange(2)+1
        if Sanjelly == 1:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n-1,w][1] = Grid[n-1,w][1] + 1
        elif Sanjelly == 2:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w+1][1] = Grid[n,w+1][1] + 1
    elif n == 1 and w == 10:
        Sanjelly = random.randrange(2)+1
        if Sanjelly == 1:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n+1,w][1] = Grid[n+1,w][1] + 1
        elif Sanjelly == 2:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w-1][1] = Grid[n,w-1][1] + 1
    elif n == 10 and w == 10:
        Sanjelly = random.randrange(2)+1
        if Sanjelly == 1:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n-1,w][1] = Grid[n-1,w][1] + 1
        elif Sanjelly == 2:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w-1][1] = Grid[n,w-1][1] + 1
    elif n == 1:
        Sanjelly = random.randrange(3)+1
        if Sanjelly == 1:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n+1,w][1] = Grid[n+1,w][1] + 1
        elif Sanjelly == 2:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w-1][1] = Grid[n,w-1][1] + 1
        elif Sanjelly == 3:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w+1][1] = Grid[n,w+1][1] + 1
    elif n == 10:
        Sanjelly = random.randrange(3)+1
        if Sanjelly == 1:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n-1,w][1] = Grid[n-1,w][1] + 1
        elif Sanjelly == 2:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w-1][1] = Grid[n,w-1][1] + 1
        elif Sanjelly == 3:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w+1][1] = Grid[n,w+1][1] + 1
    elif w == 1:
        Sanjelly = random.randrange(3)+1
        if Sanjelly == 1:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n+1,w][1] = Grid[n+1,w][1] + 1
        elif Sanjelly == 2:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n-1,w][1] = Grid[n-1,w][1] + 1
        elif Sanjelly == 3:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w+1][1] = Grid[n,w+1][1] + 1
    elif w == 10:
        Sanjelly = random.randrange(3)+1
        if Sanjelly == 1:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n+1,w][1] = Grid[n+1,w][1] + 1
        elif Sanjelly == 2:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n-1,w][1] = Grid[n-1,w][1] + 1
        elif Sanjelly == 3:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w-1][1] = Grid[n,w-1][1] + 1
    else:
        Sanjelly = random.randrange(4)+1
        if Sanjelly == 1:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w-1][1] = Grid[n,w-1][1] + 1
        elif Sanjelly == 2:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n,w+1][1] = Grid[n,w+1][1] + 1
        elif Sanjelly == 3:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n+1,w][1] = Grid[n+1,w][1] + 1
        elif Sanjelly == 4:
            Grid[n,w][1] = Grid[n,w][1] - 1
            Grid[n-1,w][1] = Grid[n-1,w][1] + 1
    return Grid

def StartingPopulace(Grid):
    print ("\nStarting Populace:")
    n = 1
    w = 1
    for i in range(10):
        Banzai = [Grid[n,w][0],Grid[n+1,w][0],Grid[n+2,w][0],Grid[n+3,w][0],Grid[n+4,w][0],Grid[n+5,w][0],Grid[n+6,w][0],Grid[n+7,w][0],Grid[n+8,w][0],Grid[n+9,w][0]]
        print (Banzai)
        w = w + 1
        
def Ultimate(Grid,n,w,potato):
    Chance = random.randrange(10)+1
    if Grid[n,w][0] >= 1:
        if Chance == 2:
            Grid = NekoMovement(Grid)
        elif Chance==3 or Chance==4 or Chance==5 or Chance==6 or Chance==7 or Chance==8 or Chance==9 or Chance==10:
            Attack = random.randrange(10)+1
            if Attack == 4 or Attack == 5:
                Grid[n,w][1] = Grid[n,w][1] - 1
            elif Attack == 6 or Attack == 7 or Attack == 8 or Attack == 9 or Attack == 10:
                Death = random.randrange(10)+1
                if Death != 1:
                    Grid[n,w][1] = Grid[n,w][1] + 1
                    Grid[n,w][0] = Grid[n,w][0] - 1
                elif Death == 1:
                    Grid[n,w][0] = Grid[n,w][0] - 1
    elif Grid[n,w][0] == 0:
        if Chance != 1:
            Grid = NekoMovement(Grid)
    potato = potato - 1
    if potato == 0:
        return Grid
    elif potato > 0:
        return Ultimate(Grid,n,w, potato)
    
def Endgame(Grid):
    repeat = 0
    for i in range(2):
        if repeat == 0:
            print ("\nHuman population:")
        elif repeat == 1:
            print ("\nZombie population:")
        n = 1
        w = 1
        for i in range(10):
            Banzai = [Grid[n,w][repeat],Grid[n+1,w][repeat],Grid[n+2,w][repeat],Grid[n+3,w][repeat],Grid[n+4,w][repeat],Grid[n+5,w][repeat],Grid[n+6,w][repeat],Grid[n+7,w][repeat],Grid[n+8,w][repeat],Grid[n+9,w][repeat]]
            print (Banzai)
            w = w + 1
        repeat = repeat + 1
        
def Discover(turn,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,J1,J2,J3,J4,J5,J6,J7,J8,J9,J10):
    if A1[0]+A2[0]+A3[0]+A4[0]+A5[0]+A6[0]+A7[0]+A8[0]+A9[0]+A10[0]+B1[0]+B2[0]+B3[0]+B4[0]+B5[0]+B6[0]+B7[0]+B8[0]+B9[0]+B10[0]+C1[0]+C2[0]+C3[0]+C4[0]+C5[0]+C6[0]+C7[0]+C8[0]+C9[0]+C10[0]+D1[0]+D2[0]+D3[0]+D4[0]+D5[0]+D6[0]+D7[0]+D8[0]+D9[0]+D10[0]+E1[0]+E2[0]+E3[0]+E4[0]+E5[0]+E6[0]+E7[0]+E8[0]+E9[0]+E10[0]+F1[0]+F2[0]+F3[0]+F4[0]+F5[0]+F6[0]+F7[0]+F8[0]+F9[0]+F10[0]+G1[0]+G2[0]+G3[0]+G4[0]+G5[0]+G6[0]+G7[0]+G8[0]+G9[0]+G10[0]+H1[0]+H2[0]+H3[0]+H4[0]+H5[0]+H6[0]+H7[0]+H8[0]+H9[0]+H10[0]+I1[0]+I2[0]+I3[0]+I4[0]+I5[0]+I6[0]+I7[0]+I8[0]+I9[0]+I10[0]+J1[0]+J2[0]+J3[0]+J4[0]+J5[0]+J6[0]+J7[0]+J8[0]+J9[0]+J10[0] == 0:
        print ("\nThe humans were exterminated in", turn, "turns.")
        DarthVader = 0
        return DarthVader
    elif A1[1]+A2[1]+A3[1]+A4[1]+A5[1]+A6[1]+A7[1]+A8[1]+A9[1]+A10[1]+B1[1]+B2[1]+B3[1]+B4[1]+B5[1]+B6[1]+B7[1]+B8[1]+B9[1]+B10[1]+C1[1]+C2[1]+C3[1]+C4[1]+C5[1]+C6[1]+C7[1]+C8[1]+C9[1]+C10[1]+D1[1]+D2[1]+D3[1]+D4[1]+D5[1]+D6[1]+D7[1]+D8[1]+D9[1]+D10[1]+E1[1]+E2[1]+E3[1]+E4[1]+E5[1]+E6[1]+E7[1]+E8[1]+E9[1]+E10[1]+F1[1]+F2[1]+F3[1]+F4[1]+F5[1]+F6[1]+F7[1]+F8[1]+F9[1]+F10[1]+G1[1]+G2[1]+G3[1]+G4[1]+G5[1]+G6[1]+G7[1]+G8[1]+G9[1]+G10[1]+H1[1]+H2[1]+H3[1]+H4[1]+H5[1]+H6[1]+H7[1]+H8[1]+H9[1]+H10[1]+I1[1]+I2[1]+I3[1]+I4[1]+I5[1]+I6[1]+I7[1]+I8[1]+I9[1]+I10[1]+J1[1]+J2[1]+J3[1]+J4[1]+J5[1]+J6[1]+J7[1]+J8[1]+J9[1]+J10[1] == 0:
        print ("\nThe zombies were exterminated in", turn, "turns.")
        DarthVader = 0
        return DarthVader
    else:
        DarthVader = 1
        return DarthVader

#main
print ("\nWelcome to A-Tamang's Zombie Simulator!\n")

badanswer = 1
while badanswer == 1:
    gamechoice = input("Would you like to run [PART A] or [PART B]? (Enter '1' or '2') --> ")
    try:
        gamechoice = int(gamechoice)
    except ValueError:
        print ("Please enter a valid entry.\n")
    if gamechoice == 1:
        badanswer = 0
        Live = "y"
        MakingLists(Grid)
        BirthOfTheZombay(Grid)
        StartingPopulace(Grid)
        while "n" not in Live:
            while True:
                Survival = input("\nFor how many turns do you want to run the simulation? --> ")
                try:
                    Survival = int(Survival)
                    if Survival > 0:
                        break
                    else:
                        print ("Please enter a valid number greater than zero.")
                except ValueError:
                    print ("Please enter a valid number greater than zero.")
            for i in range(Survival+1):
                w = 1
                for i in range(10):
                    n = 1
                    for i in range (10):
                        potato = Grid[n,w][1]
                        if potato > 0:
                            Grid = Ultimate(Grid, n,w,potato)
                        n = n+1
                    w = w+1
            Endgame(Grid)
            Live = input ("\nWould you like to continue the simulation for a few more turns?\nEnter 'n' for no, anything else for yes --> ")
    elif gamechoice == 2:
        DarthVader = 1
        turn = 0
        badanswer = 0
        MakingLists(Grid)
        StartingPopulace(Grid)
        DefineTheZombay(Grid)
        while DarthVader == 1:
            w = 1
            for i in range(10):
                n = 1
                for i in range (10):
                    potato = Grid[n,w][1]
                    if potato > 0:
                        Grid = Ultimate(Grid,n,w,potato)
                    n = n+1
                w = w+1
            turn = turn + 1
            DarthVader = Discover(turn,A1,A2,A3,A4,A5,A6,A7,A8,A9,A10,B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,C1,C2,C3,C4,C5,C6,C7,C8,C9,C10,D1,D2,D3,D4,D5,D6,D7,D8,D9,D10,E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,G1,G2,G3,G4,G5,G6,G7,G8,G9,G10,H1,H2,H3,H4,H5,H6,H7,H8,H9,H10,I1,I2,I3,I4,I5,I6,I7,I8,I9,I10,J1,J2,J3,J4,J5,J6,J7,J8,J9,J10)
        Endgame(Grid)
        
input("\nThanks for playing!")
