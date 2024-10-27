from random import *

print("Welcome, players! Are you ready for an interesting game? Let's do it!")

#Making the board of the game without any players.
Board = ["E.E.E.E.E.E.E.E.E"]
for Row in range(8):
    Line_of_dots = ""
    Line_of_empty_seats = ""
    for Column in range(9):
        Line_of_dots += ". "
        Line_of_empty_seats += "E."
    Board.append( Line_of_dots[: len( Line_of_dots ) ] )
    Board.append( Line_of_empty_seats[: len( Line_of_empty_seats ) - 1 ] )
    
#Function for moving up.
def Up1( Location ):
    #Condition of limitations.
    if Location[0] == 1 or Board[ ( Location[0] - 1 ) * 2 - 1 ][ ( Location[1] - 1 ) * 2 ] == "-":
        print("There's no seat upside! Try the other sides.")
        Side = input("Down, right, or left? < D, R, L > ")
        while Side not in ["D", "R", "L"]:
            Side = input("Down, right, or left? < D, R, L > ")
        while True:
            if Side == "D":
                Down1( Location )
                break
            elif Side == "R":
                Right1( Location )
                break
            else:
                Left1( Location )
                break
    else:
        #If your rival is above you:
        if Board[ ( Location[0] - 2 ) * 2 ][ ( Location[1] - 1 ) * 2 ] != "E":
            if Location[0] == 2 or Board[ ( Location[0] - 2 ) * 2  - 1][ ( Location[1] - 1 ) * 2 ] == "-":
                Side = input("Right or left? < R, L > ")
                while Side not in ["R", "L"]:
                    Side = input("Right or left? < R, L > ")
                if Side == "R":
                    if Location[1] == 9:
                        print("Moving right is not allowed. You'll be brought left automatedly.")
                        Location[0] -= 1
                        Location[1] -= 1
                    else:
                        Location[0] -= 1
                        Location[1] += 1
                else:
                    if Location[1] == 1:
                        print("Moving left is not allowed. You'll be brought right automatedly.")
                        Location[0] -= 1
                        Location[1] += 1
                    else:
                        Location[0] -= 1
                        Location[1] -= 1
            else:
                Location[0] -= 2
        else:
            Location[0] -= 1
            
def Up2( Location ):
    #Condition of limitations.
    if Location[0] == 1 or Board[ ( Location[0] - 1 ) * 2 - 1 ][ ( Location[1] - 1 ) * 2 ] == "-":
        Side = choice( ["D", "R", "L"] )
        while True:
            if Side == "D":
                Down2( Location )
                break
            elif Side == "R":
                Right2( Location )
                break
            else:
                Left2( Location )
                break
    else:
        #If your rival is above you:
        if Board[ ( Location[0] - 2 ) * 2 ][ ( Location[1] - 1 ) * 2 ] != "E":
            if Location[0] == 2 or Board[ ( Location[0] - 2 ) * 2  - 1][ ( Location[1] - 1 ) * 2 ] == "-":
                Side = choice( ["R", "L"] )
                if Side == "R":
                    if Location[1] == 9:
                        Location[0] -= 1
                        Location[1] -= 1
                    else:
                        Location[0] -= 1
                        Location[1] += 1
                else:
                    if Location[1] == 1:
                        Location[0] -= 1
                        Location[1] += 1
                    else:
                        Location[0] -= 1
                        Location[1] -= 1
            else:
                Location[0] -= 2
        else:
            Location[0] -= 1
            
#Function for moving down.
def Down1( Location ):
    #Condition of limitations.
    if Location[0] == 9 or Board[ ( Location[0] - 1 ) * 2 + 1 ][ ( Location[1] - 1 ) * 2 ] == "-":
        print("There's no seat downside! Try the other sides.")
        Side = input("Up, right, or left? < U, R, L > ")
        while Side not in ["U", "R", "L"]:
            Side = input("Up, right, or left? < U, R, L > ")
        while True:
            if Side == "U":
                Up1( Location )
                break
            elif Side == "R":
                Right1( Location )
                break
            else:
                Left1( Location )
                break
    else:
        #If your rival is under you:
        if Board[ Location[0] * 2 ][ ( Location[1] - 1 ) * 2 ] != "E":
            if Location[0] == 8 or Board[ Location[0] * 2 + 1 ][ ( Location[1] - 1 ) * 2 ] == "-":
                Side = input("Right or left? < R, L > ")
                while Side not in ["R", "L"]:
                    Side = input("Right or left? < R, L > ")
                if Side == "R":
                    if Location[1] == 9:
                        print("Moving right is not allowed. You'll be brought left automatedly.")
                        Location[0] += 1
                        Location[1] -= 1
                    else:
                        Location[0] += 1
                        Location[1] += 1
                else:
                    if Location[1] == 1:
                        print("Moving left is not allowed. You'll be brought right automatedly.")
                        Location[0] += 1
                        Location[1] += 1
                    else:
                        Location[0] += 1
                        Location[1] -= 1
            else:
                Location[0] += 2
        else:
            Location[0] += 1

def Down2( Location ):
    #Condition of limitations.
    if Location[0] == 9 or Board[ ( Location[0] - 1 ) * 2 + 1 ][ ( Location[1] - 1 ) * 2 ] == "-":
        Side = choice( ["U", "R", "L"] )
        while True:
            if Side == "U":
                Up2( Location )
                break
            elif Side == "R":
                Right2( Location )
                break
            else:
                Left2( Location )
                break
    else:
        #If your rival is under you:
        if Board[ Location[0] * 2 ][ ( Location[1] - 1 ) * 2 ] != "E":
            if Location[0] == 8 or Board[ Location[0] * 2 + 1 ][ ( Location[1] - 1 ) * 2 ] == "-":
                Side = choice( ["R", "L"] )
                if Side == "R":
                    if Location[1] == 9:
                        Location[0] += 1
                        Location[1] -= 1
                    else:
                        Location[0] += 1
                        Location[1] += 1
                else:
                    if Location[1] == 1:
                        Location[0] += 1
                        Location[1] += 1
                    else:
                        Location[0] += 1
                        Location[1] -= 1
            else:
                Location[0] += 2
        else:
            Location[0] += 1

#Function for moving right.
def Right1( Location ):
    #Condition of limitations.
    if Location[1] == 9 or Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) * 2 + 1 ] == "|":
        print("There's no seat rightside! Try the other sides.")
        Side = input("Up, down, or left? < U, D, L > ")
        while Side not in ["U", "D", "L"]:
            Side = input("Up, down, or left? < U, D, L > ")
        while True:
            if Side == "U":
                Up1( Location )
                break
            elif Side == "D":
                Down1( Location )
                break
            else:
                Left1( Location )
                break
    else:
        #If your rival is on your right:
        if Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) * 2 + 2 ] != "E":
            if Location[1] == 8 or Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 )* 2 + 3 ] == "|":
                Side = input("Right or left? < R, L > ")
                while Side not in ["R", "L"]:
                    Side = input("Right or left? < R, L > ")
                if Side == "L":
                    if Location[0] == 1:
                        print("Moving left is not allowed. You'll be brought your rival's right automatedly.")
                        Location[0] += 1
                        Location[1] += 1
                    else:
                        Location[0] -= 1
                        Location[1] += 1
                else:
                    if Location[0] == 9:
                        print("Moving right is not allowed. You'll be brought your rival's left automatedly.")
                        Location[0] -= 1
                        Location[1] += 1
                    else:
                        Location[0] += 1
                        Location[1] += 1
            else:
                Location[1] += 2
        else:    
            Location[1] += 1

def Right2( Location ):
    #Condition of limitations.
    if Location[1] == 9 or Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) * 2 + 1 ] == "|":
        Side = choice( ["U", "D", "L"] )
        while True:
            if Side == "U":
                Up2( Location )
                break
            elif Side == "D":
                Down2( Location )
                break
            else:
                Left2( Location )
                break
    else:
        #If your rival is on your right:
        if Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) * 2 + 2 ] != "E":
            if Location[1] == 8 or Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 )* 2 + 3 ] == "|":
                Side = choice( ["R", "L"] )
                if Side == "L":
                    if Location[0] == 1:           
                        Location[0] += 1
                        Location[1] += 1
                    else:
                        Location[0] -= 1
                        Location[1] += 1
                else:
                    if Location[0] == 9:
                        Location[0] -= 1
                        Location[1] += 1
                    else:
                        Location[0] += 1
                        Location[1] += 1
            else:
                Location[1] += 2
        else:    
            Location[1] += 1

#Function for moving left.
def Left1( Location ):
    #Condition of limitations.
    if Location[1] == 1 or Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) *  2 - 1 ] == "|":
        print("There's no seat leftside! Try the other sides.")
        Side = input("Up, down, or right? < U, D, R > ")
        while Side not in ["U", "D", "R"]:
            Side = input("Up, down, or right? < U, D, R > ")
        while True:
            if Side == "U":
                Up1( Location )
                break
            elif Side == "D":
                Down1( Location )
                break
            else:
                Right1( Location )
                break
    else:
        #If your rival is on your left:
        if Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) * 2 - 2 ] != "E":
            if Location[1] == 2 or Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) * 2 - 3 ] == "|":
                Side = input("Right or left? < R, L > ")
                while Side not in ["R", "L"]:
                    Side = input("Right or left? < R, L > ")
                if Side == "L":
                    if Location[0] == 1:
                        print("Moving left is not allowed. You'll be brought your rival's right automatedly.")
                        Location[0] += 1
                        Location[1] -= 1
                    else:
                        Location[0] -= 1
                        Location[1] -= 1
                else:
                    if Location[0] == 9:
                        print("Moving right is not allowed. You'll be brought your rival's left automatedly.")
                        Location[0] -= 1
                        Location[1] -= 1
                    else:
                        Location[0] += 1
                        Location[1] -= 1
            else:
                Location[1] -= 2
        else:
            Location[1] -= 1

def Left2( Location ):
    #Condition of limitations.
    if Location[1] == 1 or Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) *  2 - 1 ] == "|":
        Side = choice( ["U", "D", "R"] )
        while True:
            if Side == "U":
                Up2( Location )
                break
            elif Side == "D":
                Down2( Location )
                break
            else:
                Right2( Location )
                break
    else:
        #If your rival is on your left:
        if Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) * 2 - 2 ] != "E":
            if Location[1] == 2 or Board[ ( Location[0] - 1 ) * 2 ][ ( Location[1] - 1 ) * 2 - 3 ] == "|":
                Side = choice( ["R", "L"] )
                if Side == "L":
                    if Location[0] == 1:
                        Location[0] += 1
                        Location[1] -= 1
                    else:
                        Location[0] -= 1
                        Location[1] -= 1
                else:
                    if Location[0] == 9:
                        Location[0] -= 1
                        Location[1] -= 1
                    else:
                        Location[0] += 1
                        Location[1] -= 1
            else:
                Location[1] -= 2
        else:
            Location[1] -= 1
        
#The function helps the player to move.   
def Move1( Location ):
    #Selecting the side for moving at least for the first time.
    Side = input("Up, down, right, or left? < U, D, R, L > " )
    while Side not in ["U", "D", "R", "L"]:
        Side = input("Up, down, right, or left? < U, D, R, L > " )
    while True:
        if Side == "U":
            Up1( Location )
            break

        elif Side == "D":
            Down1( Location )
            break

        elif Side == "R":
            Right1( Location )
            break
        else:
            Left1( Location )
            break
        
def Move2( Location ):
    Side = choice( ["U", "D", "R", "L"] )
    while True:
        if Side == "U":
            Up2( Location )
            break

        elif Side == "D":
            Down2( Location )
            break

        elif Side == "R":
            Right2( Location )
            break
        else:
            Left2( Location )
            break

#The function helps the player to place the walls.
def Wall_picker1():
    #Selecting the direction.
    Direction = input("Vertical of horizontal? < V or H > ")
    while Direction not in ["V", "H"]:
        Direction = input("I said: 'Vertical of horizontal?' < V or H > ")
            
    if Direction == "V":
        #Selected row and next to it on its right will be occupied.
        Row = int(input("Which row? < 1 - 8 > "))
        while Row not in range(1, 9):
            Row = int(input("Out of range! Which row? < 1 - 8 > "))
        Column = int(input("Which column? < 1 - 8 > "))
        while Column not in range(1, 9):
            Column = int(input("Out of range! Which column? < 1 - 8 > "))
        while Board[ ( Row - 1 ) * 2 ][ Column * 2 - 1 ] != ".":
            print("You can't place a wall on a wall! Try again.")
            Row = int(input("Which row? < 1 - 8 > "))
            while Row not in range(1, 9):
                Row = int(input("Out of range! Which row? < 1 - 8 > "))
            Column = int(input("Which column? < 1 - 8 > "))
            while Column not in range(1, 9):
                Column = int(input("Out of range! Which column? < 1 - 8 > "))
        else:
            Board[ ( Row - 1 ) * 2 ] = Board[ ( Row - 1 ) * 2 ][: Column * 2 - 1 ] + "|" + Board[ ( Row - 1 ) * 2 ][ Column * 2 :]
            Board[ ( Row - 1 ) * 2 + 2 ] = Board[ ( Row - 1 ) * 2 + 2 ][: Column * 2 - 1 ] + "|" + Board[ ( Row - 1 ) * 2 + 2 ][ Column * 2 :]
            
    else:
        Row = int(input("Which row? < 1 - 8 > "))
        while Row not in range(1, 9):
            Row = int(input("Out of range! Which row? < 1 - 8 > "))
        #Selected column and next to it on its right will be occupied.
        Column = int(input("Which column? < 1 - 8 > "))
        while Column not in range(1, 9):
            Column = int(input("Out of range! Which column? < 1 - 8 > "))
        while Board[ Row * 2 - 1 ][( Column - 1 ) * 2 ] == "-" or Board[ Row * 2 - 1 ][ Column * 2 ] == "-": 
            print("You can't place a wall on a wall! Try again.")
            Row = int(input("Which row? < 1 - 8 > "))
            while Row not in range(1, 9):
                Row = int(input("Out of range! Which row? < 1 - 8 > "))
            Column = int(input("Which column? < 1 - 8 > "))
            while Column not in range(1, 9):
                Column = int(input("Out of range! Which column? < 1 - 8 > "))
        else:
            Board[ Row * 2 - 1 ] = Board[ Row * 2 - 1 ][: ( Column - 1 ) * 2 ] + "- -" + Board[ Row * 2 - 1 ][ Column * 2 + 1 :]
            
def Wall_picker2():
    #Selecting the direction.
    Direction = choice( ["V", "H"] )
    
    if Direction == "V":
        #Selected row and next to it on its right will be occupied.
        Row = randint(1, 8)
        Column = randint(1, 8)
        while Board[ ( Row - 1 ) * 2 ][ Column * 2 - 1 ] != ".":
            Row = randint(1, 8)
            Column = randint(1, 8)
        else:
            Board[ ( Row - 1 ) * 2 ] = Board[ ( Row - 1 ) * 2 ][: Column * 2 - 1 ] + "|" + Board[ ( Row - 1 ) * 2 ][ Column * 2 :]
            Board[ ( Row - 1 ) * 2 + 2 ] = Board[ ( Row - 1 ) * 2 + 2 ][: Column * 2 - 1 ] + "|" + Board[ ( Row - 1 ) * 2 + 2 ][ Column * 2 :]
            
    else:
        Row = randint(1, 8)
        #Selected column and next to it on its right will be occupied.
        Column = randint(1, 8)
        while Board[ Row * 2 - 1 ][( Column - 1 ) * 2 ] == "-" or Board[ Row * 2 - 1 ][ Column * 2 ] == "-": 
            Row = randint(1, 8)
            Column = randint(1, 8)
        else:
            Board[ Row * 2 - 1 ] = Board[ Row * 2 - 1 ][: ( Column - 1 ) * 2 ] + "- -" + Board[ Row * 2 - 1 ][ Column * 2 + 1 :]
            
#The function which starts the game.
def Start():
    #Preparing starting atmosphere.
    
    Location1 = [1, 5]
    Location2 = [9, 5]
    
    #              Col
    #               |
    #               v
    #Location = [i, j]
    #            ^
    #            |
    #           Row

    #Each player have ten walls at first.
    Number_of_walls1 = 10
    Number_of_walls2 = 10

    Line_of_walls1 = "| | | | | | | | | |"
    Line_of_walls2 = "| | | | | | | | | |"
    
    Board[ ( Location1[0] - 1 ) * 2 ] = Board[ ( Location1[0] - 1 ) * 2 ][: ( Location1[1] - 1 ) * 2 ] + "1" + Board[ ( Location1[0] - 1 ) * 2 ][ ( Location1[1] - 1 ) * 2 + 1 :]
    Board[ ( Location2[0] - 1 ) * 2 ] = Board[ ( Location2[0] - 1 ) * 2 ][: ( Location2[1] - 1 ) * 2 ] + "2" + Board[ ( Location2[0] - 1 ) * 2 ][ ( Location2[1] - 1 ) * 2 + 1 :]
    
    print()
    print("Your walls.")
    print(Line_of_walls1)
    print()
    for Element in Board:
        print(Element)
    print()
    print("Opponent's walls.")
    print(Line_of_walls2)
    
    while True:
        #Your turn.
        print()
        print("Your turn!")
        Choice = input("Move or Wall? < M or W > ")
        while Choice not in ["M", "W"]:
            Choice = input("I said: 'Move or Wall?' < M or W > ")
        if Choice == "M" or Number_of_walls1 == 0:
            if Number_of_walls1 == 0:
                print("Player 1. You have no wall to place. Just move!")
                
            #Cleaning your footprint.
            Board[ ( Location1[0] - 1 ) * 2 ] = Board[ ( Location1[0] - 1 ) * 2 ][: ( Location1[1] - 1 ) * 2 ] + "E" + Board[ ( Location1[0] - 1 ) * 2 ][ ( Location1[1] - 1 ) * 2 + 1 :]

            #It's time to move.
            Move1( Location1 )

            #Locating you.
            Board[ ( Location1[0] - 1 ) * 2 ] = Board[ ( Location1[0] - 1 ) * 2 ][: ( Location1[1] - 1 ) * 2 ] + "1" + Board[ ( Location1[0] - 1 ) * 2 ][ ( Location1[1] - 1 ) * 2 + 1 :]
            
        else:
            #While the player have some walls, function 'Wall_picker()' will be called.
            if Number_of_walls1 == 1:
                print("You have only a wall.")
            else:
                print("You have", Number_of_walls1, "walls.")
            Wall_picker1()
            Number_of_walls1 -= 1
            for Element in Line_of_walls1:
                if Element == "|":
                    Line_of_walls1 = Line_of_walls1[: Line_of_walls1.find( Element ) ] + "X" + Line_of_walls1[ Line_of_walls1.find( Element ) + 1 :]
                    break
            
        #Winning condition for Player 1.
        if Location1[0] == 9:
            print()
            print("Your
                  walls.")
            print(Line_of_walls1)
            print()
            for Element in Board:
                print(Element)
            print()
            print("Opponent's walls.")
            print(Line_of_walls2)
            print()
            print("You win!")
            break
    
        #If the path become closed, the game will be stopped.
        #if "- - - - - - - - - " in Board and ( ( Location1[0] - 1 ) * 2 < Board.index( "- - - - - - - - - " ) or ( Location2[0] - 1 ) * 2 > Board.index( "- - - - - - - - - " ) ):
            #print("Path is closed; so the game must be stopped.")
            #break
    
        #Opponent's turn.
        Choice = choice( ["M", "W"] )
        if Choice == "M" or Number_of_walls2 == 0:
            #Cleaning your opponent's footprint.
            Board[ ( Location2[0] - 1 ) * 2 ] = Board[ ( Location2[0] - 1 ) * 2 ][: ( Location2[1] - 1 ) * 2 ] + "E" + Board[ ( Location2[0] - 1 ) * 2 ][ ( Location2[1] - 1 ) * 2 + 1 :]
            
            #It's time to move.
            Move2( Location2 )

            #Locating your opponent.
            Board[ ( Location2[0] - 1 ) * 2 ] = Board[ ( Location2[0] - 1 ) * 2 ][: ( Location2[1] - 1 ) * 2 ] + "2" + Board[ ( Location2[0] - 1 ) * 2 ][ ( Location2[1] - 1 ) * 2 + 1 :]
            
        else:
            #While the player have some walls, function 'Wall_picker()' will be called.
            Wall_picker2()
            Number_of_walls2 -= 1
            for Element in Line_of_walls2:
                if Element == "|":
                    Line_of_walls2 = Line_of_walls2[: Line_of_walls2.find( Element ) ] + "X" + Line_of_walls2[ Line_of_walls2.find( Element ) + 1 :]
                    break
        print()
        print("Your walls.")
        print(Line_of_walls1)
        print()
        for Element in Board:
            print(Element)
        print()
        print("Opponent's walls.")
        print(Line_of_walls2)
        
        #Winning condition for your opponent.
        if Location2[0] == 1:
            print()
            print("Opponent wins!")
            break
    
        #If the path become closed, the game will be stopped.
        #if "- - - - - - - - - " in Board and ( ( Location1[0] - 1 ) * 2 < Board.index( "- - - - - - - - - " ) or ( Location2[0] - 1 ) * 2 > Board.index( "- - - - - - - - - " ) ):
            #print("Path is closed; so the game must be stopped.")
            #break

#Playing the game for the first time.
Start()
        
#Having the ability to try again without running again.
while True:
    print("----------------------------------------")
    Try = input("Do you want to try again? < Y or N > ")
    while Try not in ["Y", "N"]:
        Try = input("Do you want to try again or not? < Y or N > ")
    if Try == "Y":
        #Equipping the starting atmosphere again.
        Board = ["E.E.E.E.E.E.E.E.E"]
        for Row in range(8):
            Line_of_dots = ""
            Line_of_empty_seats = ""
            for Column in range(9):
                Line_of_dots += ". "
                Line_of_empty_seats += "E."
            Board.append( Line_of_dots[: len( Line_of_dots ) ] )
            Board.append( Line_of_empty_seats[: len( Line_of_empty_seats ) - 1 ] )

        #Starting the game for another time.
        Start()

    else:
        break
              
print("Have fun ;)")
#THE-END 


